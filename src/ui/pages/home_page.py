import logging
from src.ui.pages.base_page import BasePage
from src.ui.pages.search_page import SearchPage

logger = logging.getLogger()


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        'search_field': ('ID', "search-input"),
        'search_button': ('ID', "search-submit")
    }

    def search(self, driver, advertisement_search_string):
        logger.info('Enter data to search')
        self.search_field.send_keys(advertisement_search_string)
        logger.info('Click search button')
        self.search_button.click()
        return SearchPage(driver)
