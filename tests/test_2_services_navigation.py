import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_navigation_to_products(driver):
    driver.get("https://www.kaspersky.ru")
    wait = WebDriverWait(driver, 15)

    business_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(), 'Для среднего бизнеса') or contains(text(), 'Для бизнеса')]")
    ))
    business_button.click()
    time.sleep(1)
#разные варианты поиска разных элементов сделаны из за разных версий сайта, которые открываются локально и через селеноид
    try:
        small_business = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'HeaderBBB_mainMenuTabContentWrapperBg')]//a[contains(@href, 'small-business')]"
            )
        ))
        small_business.click()
    except:
        small_business = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@href, '/small-business-security')]")
        ))
        small_business.click()

    wait.until(EC.url_contains("small-business"))
    assert "small-business" in driver.current_url