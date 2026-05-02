import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(self.driver.base_url)
        return self

    @allure.step("Проверить наличие карточек продуктов")
    def verify_product_cards_presence(self):
        cards = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[class*='product']"))
        )
        assert len(cards) > 0
        return self

    @allure.step("Нажать кнопку 'Для дома'")
    def click_for_home(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Для дома')]")
            )
        )
        button.click()
        time.sleep(0.5)
        return self

    @allure.step("Нажать 'Смотреть все решения'")
    def click_all_solutions(self):
        link = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(text(), 'Смотреть все решения')]")
            )
        )
        link.click()
        return self

    @allure.step("Проверить колонки защиты")
    def verify_protection_columns(self):
        columns = ["Максимальная защита", "Оптимальная защита", "Базовая защита"]
        for column in columns:
            element = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//*[contains(text(), '{column}')]")
                )
            )
            assert element.is_displayed()
        return self

    @allure.step("Прокрутить до кнопок 'Купить'")
    def scroll_to_buy_buttons(self):
        self.driver.execute_script("window.scrollBy(0, 1200);")
        time.sleep(1)
        return self

    @allure.step("Проверить наличие кнопок 'Купить'")
    def verify_buy_buttons_count(self, min_count=3):
        buttons = self.driver.find_elements(
            By.XPATH, "//button[@data-at-selector='buy-block-buy-button']"
        )
        assert len(buttons) >= min_count
        return self

    @allure.step("Нажать первую кнопку 'Купить'")
    def click_first_buy_button(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@data-at-selector='buy-block-buy-button']")
            )
        )
        self.driver.execute_script("arguments[0].click();", button)
        return self

    @allure.step("Проверить заголовок формы")
    def verify_form_title(self, expected_text):
        text_element = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[@data-i18nkey='components.Personal.title']")
            )
        )
        assert expected_text in text_element.text
        return self
