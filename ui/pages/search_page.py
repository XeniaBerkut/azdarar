import logging
from datetime import date, timedelta, datetime

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from ui.entities.advertisement import Advertisement

logger = logging.getLogger()


class SearchPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def collect_results(self, advertisement, depth) -> list[Advertisement]:
        logger.info('Collect results list')
        main_form = self.driver.find_element(By.ID, 'content')
        results_list = main_form.find_elements(By.CLASS_NAME, 'items')
        ads_list = []
        logger.info('Start to collect ads_list')
        depth_date = datetime.now() - timedelta(days=depth)

        for i in range(100):
            date_field = results_list[i].find_element(By.CLASS_NAME, 'dates')
            ad_date = datetime.strptime(date_field.text, "%d.%m.%Y")
            if ad_date > depth_date:
                ads_list.append(Advertisement(ad_type=advertisement.ad_type,
                                              ad_search_string=advertisement.ad_search_string,
                                              ad_date=ad_date,
                                              ad_link=results_list[i].find_element(By.XPATH, '//h3/a').get_attribute("href")))
                # ads_list.append(results_list[i].find_element(By.XPATH, '//h3/a').get_attribute("href"))
        logger.info('Finished to collect ads_list')
        return ads_list
