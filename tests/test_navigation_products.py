import allure
from pages.home_page import HomePage
from pages.navigation_page import NavigationPage
from pages.products_page import ProductsPage
from pages.search_page import SearchPage


@allure.title("Проверка заголовка главной страницы")
@allure.feature("Главная страница")
@allure.severity(allure.severity_level.NORMAL)
def test_homepage_title(driver):
    title = HomePage(driver).open().get_title()
    assert "Лаборатория Касперского" in title


@allure.title("Навигация к странице продуктов")
@allure.feature("Навигация")
@allure.severity(allure.severity_level.NORMAL)
def test_navigation_to_products(driver):
    (
        NavigationPage(driver)
        .open()
        .click_business_button()
        .click_small_business()
        .verify_small_business_url()
    )


@allure.title("Проверка наличия карточек продуктов")
@allure.feature("Карточки продуктов")
@allure.severity(allure.severity_level.NORMAL)
def test_product_cards_presence(driver):
    (ProductsPage(driver).open().verify_product_cards_presence())


@allure.title("Поиск по слову 'антивирус'")
@allure.feature("Поиск")
@allure.severity(allure.severity_level.NORMAL)
def test_search(driver):
    (
        SearchPage(driver)
        .open()
        .open_search_form()
        .search("антивирус")
        .verify_results_exist()
    )
