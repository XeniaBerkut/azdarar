from selenium.webdriver.chrome.webdriver import WebDriver
from seleniumpagefactory.Pagefactory import PageFactory


class BasePage(PageFactory):
    def __init__(self, driver: WebDriver):
        self.driver = driver
