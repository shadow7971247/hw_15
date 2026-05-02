import allure


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(self.driver.base_url)
        return self

    @allure.step("Получить заголовок страницы")
    def get_title(self):
        return self.driver.title
