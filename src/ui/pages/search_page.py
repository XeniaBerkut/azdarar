import logging

from ui.elements.avertisement_item import AdvertisementItem
from ui.pages.base_page import BasePage
from datetime import timedelta, datetime

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from ui.entities.advertisement import Advertisement

logger = logging.getLogger()


class SearchPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    locators = {
        'main_content_form': ('ID', "content")
    }

    def get_advertisements_list(self) -> list[AdvertisementItem]:
        raw_elements = self.main_content_form.find_elements(By.CLASS_NAME, 'items')
        advertisements = [AdvertisementItem(element) for element in raw_elements]
        return advertisements

    def collect_results(self, advertisement, depth, ads_category) -> list[Advertisement]:
        logger.info('Collect search results list')
        search_results_list = self.get_advertisements_list()
        ads_list = []
        depth_date = datetime.now() - timedelta(days=depth)

        logger.info('Start to collect advertisements list')
        for result in search_results_list:
            ad_date = result.get_ad_date()
            if (ad_date > depth_date) & result.advertisement_category_is_right(ads_category):
                ads_list.append(Advertisement(ad_type=advertisement.ad_type,
                                              ad_search_string=advertisement.ad_search_string,
                                              ad_date=ad_date.strftime("%d.%m.%Y"),
                                              ad_link=result.get_ad_link()
                                              ))
        logger.info('Finished to collect advertisements list')

        return sorted(ads_list, key=lambda x: x.ad_date, reverse=True)
