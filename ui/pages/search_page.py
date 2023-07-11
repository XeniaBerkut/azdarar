import logging
from time import strptime

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


logger = logging.getLogger()

class SearchPage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def collect_results(self) -> list:
        logger.info('Collect results list')
        results_list = self.driver.find_elements(By.XPATH, '//*[@id="content"]/div')
        # for element in results_list:
        #     link = element.find_element(By.XPATH, '//h3/a')
        #     logger.info(link.get_attribute('href'))
        for i in range(0, 101):
            # date = results_list[i].find_element(By.CLASS_NAME, 'dates')
            # if strptime(date.text) < :
            logger.info('Find a link')
            link = results_list[i].find_element(By.XPATH, '//h3/a')
            logger.info('Go by link')
            link.click()
            logger.info('Go back to the search page')
            self.driver.back()




