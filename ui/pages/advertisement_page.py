import logging
from ui.pages.base_page import BasePage

logger = logging.getLogger()


class AdvertisementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        'ad_text': ('XPATH', '//*[@id="item-content"]/p')
    }

    def go_to_ad_page(self, link):
        # logger.info('Go to the add page')
        self.driver.get(link)

    def get_ad_text(self) -> str:
        # logger.info('Get ad text')
        return self.ad_text.get_text()
