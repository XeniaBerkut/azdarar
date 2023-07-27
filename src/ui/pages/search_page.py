import logging
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

    def collect_results(self, advertisement, depth) -> list[Advertisement]:
        logger.info('Collect search results list')
        results_list = self.main_content_form.find_elements(By.CLASS_NAME, 'items')
        ads_list = []
        depth_date = datetime.now() - timedelta(days=depth)

        logger.info('Start to collect advertisements list')
        for result in results_list:
            date_field = result.find_element(By.CLASS_NAME, 'dates')
            ad_date = datetime.strptime(date_field.text, "%d.%m.%Y")
            if ad_date > depth_date:
                ads_list.append(Advertisement(ad_type=advertisement.ad_type,
                                              ad_search_string=advertisement.ad_search_string,
                                              ad_date=ad_date.strftime("%d.%m.%Y"),
                                              ad_link=result.find_element(By.CSS_SELECTOR, 'h3 > a')
                                              .get_attribute("href")
                                              ))
        logger.info('Finished to collect advertisements list')

        return ads_list
