from ui.pages.home_page import HomePage
from ui.pages.search_page import SearchPage
from ui.pages.advertisement_page import AdvertisementPage
from helpers.spreadsheet_helpers import write_ads_search_result_to_excel
from ui.entities.advertisement import Advertisement
import json
import os
import pytest


def get_data() -> list[Advertisement]:
    json_path = os.path.join(os.path.dirname(__file__),
                             "test_data_search_advertisement.json")
    with open(json_path) as json_file:
        data = json.load(json_file)
    return data


@pytest.mark.parametrize("advertisement_data", get_data())
def test_search(driver, advertisement_data):

    advertisement = Advertisement(**advertisement_data)

    home_page: HomePage = HomePage(driver)
    search_page: SearchPage = SearchPage(driver)
    ad_page: AdvertisementPage = AdvertisementPage(driver)
    home_page.search_home_page(advertisement.ad_search_string)
    advertisements_list = search_page.collect_results(advertisement, depth=31)
    results = []
    for ad in advertisements_list:
        ad_page.go_to_ad_page(ad.ad_link)
        ad_text = ad_page.get_ad_text()
        ad.ad_text = ad_text
    write_ads_search_result_to_excel(advertisements_list, advertisement.ad_type)
    assert advertisements_list != []
