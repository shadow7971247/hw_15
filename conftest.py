import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from dotenv import load_dotenv
from utils import attach

load_dotenv()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", choices=["chrome", "firefox", "edge"]
    )
    parser.addoption("--browser_version", default="128.0")
    parser.addoption("--headless", action="store_true", default=False)
    parser.addoption("--width", default="1920")
    parser.addoption("--height", default="1080")
    parser.addoption(
        "--base_url", default=os.getenv("BASE_URL", "https://www.kaspersky.ru")
    )
    parser.addoption(
        "--selenoid_url",
        default=os.getenv("SELENOID_URL", "selenoid.autotests.cloud/wd/hub"),
    )


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    browser_version = request.config.getoption("--browser_version")
    headless = request.config.getoption("--headless") == "True"
    width = request.config.getoption("--width")
    height = request.config.getoption("--height")
    base_url = request.config.getoption("--base_url")
    selenoid_url = request.config.getoption("--selenoid_url")

    remote_url = _build_remote_url(selenoid_url)
    options = _create_browser_options(browser_name, headless, width, height)
    _add_selenoid_capabilities(options, browser_name, browser_version)

    driver = (
        webdriver.Remote(command_executor=remote_url, options=options)
        if remote_url
        else _create_local_driver(browser_name, options)
    )

    driver.implicitly_wait(10)
    driver.base_url = base_url

    yield driver

    _attach_and_quit(driver)


def _build_remote_url(selenoid_url):
    if not selenoid_url:
        return ""
    if not selenoid_url.startswith(("http://", "https://")):
        selenoid_url = f"https://{selenoid_url}"
    user = os.getenv("SELENOID_USER", "")
    password = os.getenv("SELENOID_PASSWORD", "")
    if user and password:
        selenoid_url = selenoid_url.replace("://", f"://{user}:{password}@")
    return selenoid_url


def _create_browser_options(browser_name, headless, width, height):
    if browser_name == "chrome":
        options = Options()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument(f"--window-size={width},{height}")
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument(f"--width={width}")
        options.add_argument(f"--height={height}")
    elif browser_name == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument(f"--window-size={width},{height}")
    else:
        raise ValueError(f"Browser {browser_name} not supported")
    return options


def _add_selenoid_capabilities(options, browser_name, browser_version):
    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": browser_version,
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }
    options.capabilities.update(selenoid_capabilities)


def _create_local_driver(browser_name, options):
    if browser_name == "chrome":
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager

        return webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )
    elif browser_name == "firefox":
        from selenium.webdriver.firefox.service import Service
        from webdriver_manager.firefox import GeckoDriverManager

        return webdriver.Firefox(
            service=Service(GeckoDriverManager().install()), options=options
        )
    elif browser_name == "edge":
        from selenium.webdriver.edge.service import Service
        from webdriver_manager.microsoft import EdgeChromiumDriverManager

        return webdriver.Edge(
            service=Service(EdgeChromiumDriverManager().install()), options=options
        )


def _attach_and_quit(driver):
    try:
        for attach_func in [
            attach.add_screenshot,
            attach.add_page_source,
            attach.add_console_logs,
            attach.add_video,
        ]:
            try:
                attach_func(driver)
            except Exception:
                pass
        driver.quit()
    except Exception:
        pass
