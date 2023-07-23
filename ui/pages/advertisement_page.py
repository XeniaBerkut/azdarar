import logging
from ui.pages.base_page import BasePage

logger = logging.getLogger()


class AdvertisementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        'ad_text': ('ID', 'content')
    }

    def go_to_ad_page(self, link):
        logger.debug(f'Go to the advertisement page {link}')
        self.driver.get(link)

    def get_ad_text(self) -> str:
        logger.debug('Get advertisement text with HTML layout')
        return self.ad_text.getAttribute('outerHTML')
