import json
import os
import logging
import pytest

from selenium.webdriver.chrome.webdriver import WebDriver
from ui.pages.home_page import HomePage
from ui.pages.search_page import SearchPage
from ui.pages.advertisement_page import AdvertisementPage
from helpers.output_helpers import write_ads_search_result_to_html
from ui.entities.advertisement import Advertisement


def get_data(file_name) -> list[dict]:
    json_path = os.path.join(os.path.dirname(__file__),
                             file_name)
    with open(json_path, encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


@pytest.mark.parametrize("advertisement_data", get_data("test_search_advertisements_data.json"))
def test_search(driver: WebDriver, config: dict, advertisement_data: dict):
    advertisement = Advertisement(**advertisement_data)

    home_page: HomePage = HomePage(driver)
    ad_page: AdvertisementPage = AdvertisementPage(driver)

    logging.info(f'Start search with search data {advertisement.ad_search_string}')
    search_page = home_page.search(driver, advertisement.ad_search_string)

    logging.info('Collect advertisements links for specified search data')
    advertisements_list = search_page.collect_results(advertisement,
                                                      config['search_date_depth'],
                                                      config['ads_category'])
    advertisements_list = search_page.collect_results(advertisement, config['search_date_depth'])

    logging.info('Go to advertisements pages and collect advertisements outerTexts')
    for ad in advertisements_list:
        ad_page.go_to_ad_page(driver, ad.ad_link)
        ad_text = ad_page.get_ad_text()
        ad.ad_text = ad_text
    logging.info('Finished to collect advertisements texts')

    output_folder_name = config['output_folder']
    logging.info('Write results to html file')
    write_ads_search_result_to_html(advertisements_list, advertisement.ad_type, output_folder_name)

    assert advertisements_list != []
