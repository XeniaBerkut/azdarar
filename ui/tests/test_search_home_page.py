import json
import logging
import os
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from ui.pages.home_page import HomePage
from ui.pages.search_page import SearchPage
from ui.pages.advertisement_page import AdvertisementPage
from helpers.output_helpers import write_ads_search_result_to_excel
from helpers.output_helpers import write_ads_search_result_to_html
from ui.entities.advertisement import Advertisement


def get_data() -> list[dict]:
    json_path = os.path.join(os.path.dirname(__file__),
                             "test_data_search_advertisement.json")
    with open(json_path, encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


@pytest.mark.parametrize("advertisement_data", get_data())
def test_search(driver: WebDriver, advertisement_data: dict):

    advertisement = Advertisement(**advertisement_data)

    home_page: HomePage = HomePage(driver)
    search_page: SearchPage = SearchPage(driver)
    ad_page: AdvertisementPage = AdvertisementPage(driver)
    logging.info(f'search string {advertisement.ad_search_string}')
    home_page.search_home_page(advertisement.ad_search_string)
    advertisements_list = search_page.collect_results(advertisement, depth=7)
    for ad in advertisements_list:
        ad_page.go_to_ad_page(ad.ad_link)
        ad_text = ad_page.get_ad_text()
        ad.ad_text = ad_text
    write_ads_search_result_to_excel(advertisements_list, advertisement.ad_type)
    write_ads_search_result_to_html(advertisements_list, advertisement.ad_type)
    assert advertisements_list != []
