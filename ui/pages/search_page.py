import logging
from datetime import timedelta, datetime

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from ui.entities.advertisement import Advertisement

logger = logging.getLogger()


class SearchPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def collect_results(self, advertisement, depth) -> list[Advertisement]:
        logger.info('Collect search results list')
        main_form = self.driver.find_element(By.ID, 'content')
        results_list = main_form.find_elements(By.CLASS_NAME, 'items')
        ads_list = []
        depth_date = datetime.now() - timedelta(days=depth)

        logger.info('Start to collect advertisements list')
        for result in results_list:
            date_field = result.find_element(By.CLASS_NAME, 'dates')
            ad_date = datetime.strptime(date_field.text, "%d.%m.%Y")
            link_css_selector = 'h3 > a'
            if ad_date > depth_date:
                ads_list.append(Advertisement(ad_type=advertisement.ad_type,
                                              ad_search_string=advertisement.ad_search_string,
                                              ad_date=ad_date.strftime("%d.%m.%Y"),
                                              ad_link=result.find_element(By.CSS_SELECTOR, link_css_selector)
                                              .get_attribute("href")))

        logger.info('Finished to collect advertisements list')
        return ads_list
