def test_homepage_title(driver):
    driver.get("https://www.kaspersky.ru")
    title = driver.title
    assert "Касперского" in title