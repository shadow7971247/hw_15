import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(self.driver.base_url)
        return self

    @allure.step("Открыть форму поиска")
    def open_search_form(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[aria-label='Открыть условия поиска']")
            )
        )
        button.click()
        time.sleep(0.5)
        return self

    @allure.step("Выполнить поиск {query}")
    def search(self, query):
        search_input = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[contains(@class, 'Search_input')]")
            )
        )
        search_input.send_keys(query)
        search_input.send_keys(Keys.RETURN)
        time.sleep(2)
        return self

    @allure.step("Проверить наличие результатов поиска")
    def verify_results_exist(self):
        try:
            self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'ResultList')]")
                )
            )
            results = self.driver.find_elements(
                By.XPATH, "//div[contains(@class, 'ResultList_title')]"
            )
            assert len(results) > 0
        except TimeoutError:
            no_results = self.driver.find_elements(
                By.XPATH,
                "//*[contains(text(), 'ничего не найдено') or contains(text(), 'No results')]",
            )
            if no_results:
                assert False
            raise
        return self
