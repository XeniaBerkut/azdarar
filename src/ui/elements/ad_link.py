from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class AdLink(WebElement):
    def get_ad_link(self) -> str:
        return self.find_element(By.CSS_SELECTOR, 'h3 > a').get_attribute("href")
