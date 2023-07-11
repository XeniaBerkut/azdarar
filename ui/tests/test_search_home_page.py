from ui.pages.home_page import HomePage
from ui.pages.search_page import SearchPage

def test_search(driver):
    home_page: HomePage = HomePage(driver)
    search_page: SearchPage = SearchPage(driver)
    home_page.search_home_page("աճուրդ-վաճառքի")
    search_page.collect_results()
    assert driver.current_url == 'https://www.azdarar.am/search/'
