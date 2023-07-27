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
        link_locator = 'h3 > a'

        logger.info('Collect search results list')
        results_list = self.main_content_form.find_elements(By.CLASS_NAME, 'items')
        ads_list = []
        depth_date = datetime.now() - timedelta(days=depth)

        logger.info('Start to collect advertisements list')
        for result in results_list:
            date_field = result.find_element(By.CLASS_NAME, 'dates')
            ad_date = datetime.strptime(date_field.text, "%d.%m.%Y")
            tags = result.find_elements(By.TAG_NAME, 'a')
            advertisement_category_is_right = False
            for tag in tags:
                if tag.text == ads_category:
                    advertisement_category_is_right = True

            if (ad_date > depth_date) & advertisement_category_is_right:
                ads_list.append(Advertisement(ad_type=advertisement.ad_type,
                                              ad_search_string=advertisement.ad_search_string,
                                              ad_date=ad_date.strftime("%d.%m.%Y"),
                                              ad_link=result.find_element(By.CSS_SELECTOR, link_locator)
                                              .get_attribute("href")
                                              ))
        logger.info('Finished to collect advertisements list')

        return ads_list
