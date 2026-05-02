import allure
from pages.products_page import ProductsPage


@allure.feature("Карточки продуктов")
@allure.severity(allure.severity_level.CRITICAL)
def test_product_card_details(driver):
    (
        ProductsPage(driver)
        .open()
        .click_for_home()
        .click_all_solutions()
        .verify_protection_columns()
        .scroll_to_buy_buttons()
        .verify_buy_buttons_count(3)
        .click_first_buy_button()
        .verify_form_title("Укажите ваши данные")
    )
