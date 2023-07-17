import logging
from time import strptime

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


logger = logging.getLogger()


class SearchPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def collect_results(self) -> list:
        logger.info('Collect results list')
        results_list = self.driver.find_elements(By.XPATH, '//*[@id="content"]/div/h3/a')
        links = []
        for i in range(0, 100):
            # TODO date = results_list[i].find_element(By.CLASS_NAME, 'dates')
            logger.info('Collect links')
            links.append(results_list[i].get_attribute("href"))
        return links
