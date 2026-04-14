from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_product_cards_presence(driver):
    driver.get("https://www.kaspersky.ru")
    wait = WebDriverWait(driver, 2)

    product_cards = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "[class*='product']")
    ))
    assert len(product_cards) > 0