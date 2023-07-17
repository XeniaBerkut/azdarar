from ui.pages.home_page import HomePage
from ui.pages.search_page import SearchPage
from ui.pages.advertisement_page import AdvertisementPage
from helpers.spreadsheet_helpers import write_advertisements_search_result_to_excel
from ui.entities.advertisement import Advertisement
import json
import os


def test_search(driver):
    json_path = os.path.join(os.path.dirname(__file__),
                             "test_data_search_advertisement.json")
    with open(json_path) as json_file:
        data = json.load(json_file)

    advertisement = Advertisement(**data["advertisement"])

    home_page: HomePage = HomePage(driver)
    search_page: SearchPage = SearchPage(driver)
    ad_page: AdvertisementPage = AdvertisementPage(driver)
    home_page.search_home_page(advertisement.ad_type)
    links = search_page.collect_results()
    results = []
    for link in links:
        ad_page.go_to_ad_page(link)
        ad_text = ad_page.get_ad_text()
        results.append([link, ad_text])
    write_advertisements_search_result_to_excel(results)
    assert results != []
