from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.ui.entities.enums.advertisements_categories import Categories


class AdvertisementItem:
    def __init__(self, element: WebElement):
        self._element = element

    def get_ad_link(self) -> str:
        return self._element.find_element(By.CSS_SELECTOR, 'h3 > a').get_attribute("href")

    def get_ad_date(self) -> datetime:
        date_field = self._element.find_element(By.CLASS_NAME, 'dates')
        return datetime.strptime(date_field.text, "%d.%m.%Y")

    def advertisement_category_is_right(self, category: Categories) -> bool:
        tags = self._element.find_elements(By.TAG_NAME, 'a')
        advertisement_category_is_right = False
        for tag in tags:
            if tag.text == category.value:
                advertisement_category_is_right = True
        return advertisement_category_is_right

    def get_element(self) -> WebElement:
        return self._element
