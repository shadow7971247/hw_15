
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_product_card_details(driver):
    driver.get("https://www.kaspersky.ru")
    wait = WebDriverWait(driver, 10)

    for_home = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(), 'Для дома')]")
    ))
    for_home.click()
    time.sleep(0.5)

    all_solutions = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//a[contains(text(), 'Смотреть все решения')]")
    ))
    all_solutions.click()

    max_protection = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[contains(text(), 'Максимальная защита')]")
    ))
    assert max_protection.is_displayed()

    optimal_protection = driver.find_element(By.XPATH, "//*[contains(text(), 'Оптимальная защита')]")
    assert optimal_protection.is_displayed()

    basic_protection = driver.find_element(By.XPATH, "//*[contains(text(), 'Базовая защита')]")
    assert basic_protection.is_displayed()

    driver.execute_script("window.scrollBy(0, 1200);")
    time.sleep(1)

    buy_buttons = driver.find_elements(By.XPATH, "//button[@data-at-selector='buy-block-buy-button']")
    assert len(buy_buttons) >= 3

    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-at-selector='buy-block-buy-button']")))
    driver.execute_script("arguments[0].click();", button)

    text_element = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[@data-i18nkey='components.Personal.title']")
    ))
    assert "Укажите ваши данные" in text_element.text