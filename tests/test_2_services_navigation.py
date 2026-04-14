import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_navigation_to_products(driver):
    driver.get("https://www.kaspersky.ru")
    wait = WebDriverWait(driver, 15)

    business_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(), 'Для бизнеса') or contains(., 'Для бизнеса')]")
    ))
    business_button.click()

    time.sleep(1)

    small_business = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[contains(@class, 'FullSectionItem_title') and contains(text(), 'Для малого бизнеса')]")
    ))
    small_business.click()

    wait.until(EC.url_contains("small-business"))
