import pytest
from selenium import webdriver
from config import SELENIUM_SERVER_URL, HOST, HEADLESS


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    if HEADLESS:
        options.add_argument("--headless")
    driver = webdriver.Remote(
        command_executor=SELENIUM_SERVER_URL,
        options=options
    )
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def front_host():
    return HOST

