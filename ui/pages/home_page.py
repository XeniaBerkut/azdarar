import logging
from ui.pages.base_page import BasePage

logger = logging.getLogger()


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        'search_field': ('ID', "search-input"),
        'search_button': ('ID', "search-submit")
    }

    def search_home_page(self, staff):
        logger.info('Enter data to search')
        self.search_field.send_keys(staff)
        logger.info('Click search button')
        self.search_button.click()
