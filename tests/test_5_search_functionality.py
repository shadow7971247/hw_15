import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search(driver):
    driver.get("https://www.kaspersky.ru")
    wait = WebDriverWait(driver, 5)

    search_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[aria-label='Открыть условия поиска']")
    ))
    search_button.click()
    time.sleep(0.5)

    search_input = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input.Search_input__p54_D")
    ))
    search_input.send_keys("антивирус")
    search_input.send_keys(Keys.RETURN)
    results_container = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "ResultList_scrollContent__eWhzj")
    ))
    assert results_container.is_displayed()

    results = driver.find_elements(By.CSS_SELECTOR, ".ResultList_title__GY07Z")
    assert len(results) > 0
