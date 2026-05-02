import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NavigationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(self.driver.base_url)
        return self

    @allure.step("Нажать кнопку 'Для бизнеса'")
    def click_business_button(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(text(), 'Для среднего бизнеса') or contains(text(), 'Для бизнеса')]",
                )
            )
        )
        button.click()
        return self

    @allure.step("Выбрать 'Малый бизнес'")
    def click_small_business(self):
        try:
            element = self.wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//div[contains(@class, 'HeaderBBB_mainMenuTabContentWrapperBg')]//a[contains(@href, 'small-business')]",
                    )
                )
            )
            element.click()
        except:
            element = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[contains(@href, '/small-business-security')]")
                )
            )
            element.click()
        return self

    @allure.step("Проверить URL страницы малого бизнеса")
    def verify_small_business_url(self):
        self.wait.until(EC.url_contains("small-business"))
        assert "small-business" in self.driver.current_url
        return self
