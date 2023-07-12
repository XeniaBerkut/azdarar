from ui.pages.home_page import HomePage
from ui.pages.search_page import SearchPage
from ui.pages.ad_page import AdPage
from ui.entities.ads import write_to_excel

def test_search(driver):
    home_page: HomePage = HomePage(driver)
    search_page: SearchPage = SearchPage(driver)
    ad_page: AdPage = AdPage(driver)
    home_page.search_home_page("աճուրդ-վաճառքի")
    links = search_page.collect_results()
    results = []
    for link in links:
        ad_page.go_to_ad_page(link)
        ad_text = ad_page.get_ad_text()
        results.append([link, ad_text])
    write_to_excel(results)
    assert results != []
    # assert driver.current_url == 'https://www.azdarar.am/search/'
