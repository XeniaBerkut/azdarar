import os
import logging
import pytest

from selenium.webdriver.chrome.webdriver import WebDriver

from helpers.test_data_helpers import get_test_data_from_json
from ui.entities.enums.advertisements_categories import Categories
from ui.pages.home_page import HomePage
from ui.pages.advertisement_page import AdvertisementPage
from helpers.output_helpers import write_ads_search_result_to_html, send_email
from ui.entities.advertisement import Advertisement

logger = logging.getLogger()

test_data_file_path = os.path.join(os.path.dirname(__file__), "test_search_advertisements_data.json")


@pytest.mark.run(order=1)
@pytest.mark.parametrize("advertisement_data", get_test_data_from_json(test_data_file_path))
def test_search(driver: WebDriver, config: dict, advertisement_data: dict):
    advertisement = Advertisement(**advertisement_data)

    home_page: HomePage = HomePage(driver)
    ad_page: AdvertisementPage = AdvertisementPage(driver)

    logger.info(f'Start search with search data {advertisement.ad_search_string}')
    search_page = home_page.search(driver, advertisement.ad_search_string)

    logger.info('Collect advertisements links for specified search data')
    advertisements_list = search_page.collect_results(advertisement,
                                                      config['search_date_depth'],
                                                      Categories.PUBLIC_AUCTIONS)

    logger.info('Go to advertisements pages and collect advertisements outerTexts')
    for ad in advertisements_list:
        ad_page.go_to_ad_page(driver, ad.ad_link)
        ad_text = ad_page.get_ad_text()
        ad.ad_text = ad_text
    logger.info('Finished to collect advertisements texts')

    output_folder_name = config['output_folder']
    logger.info('Write results to html file')
    write_ads_search_result_to_html(advertisements_list, advertisement.ad_type, output_folder_name)

    assert advertisements_list != []


@pytest.mark.run(order=2)
def test_send_email(config):
    logger.info("Define paths")
    data_folder_path = os.path.dirname(__file__)
    attachments_directory_path = os.path.join(data_folder_path, "azdarar_search_results")
    email_body_data = get_test_data_from_json(test_data_file_path)

    logger.info("Check if existed files count is as expected")
    expected_results_count = len(email_body_data)
    results_count = len(os.listdir(attachments_directory_path))
    assert expected_results_count == results_count

    logger.info("Sending email with results")
    send_email(data_folder_path, attachments_directory_path, email_body_data, config["search_date_depth"])
