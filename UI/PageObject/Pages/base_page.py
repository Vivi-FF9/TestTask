from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Source.users import User
from UI.PageObject.Locators.main_header_locators import MainHeaderLocators
from UI.PageObject.Locators.start_page_locators import StartPageLocators
from UI.PageObject.Locators.login_page_locators import LoginPageLocators


class MainHeader:
    def __init__(self, driver: WebDriver, host: str):
        self.driver = driver
        self.host = host

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_home(self):
        self.find_element(MainHeaderLocators.HOME_BUTTON).click()

    def logout(self):
        self.find_element(MainHeaderLocators.LOGOUT_BUTTON).click()


class BasePage:
    def __init__(self, driver: WebDriver, host: str):
        self.driver = driver
        self.host = host
        self.url = None
        self.MainHeaderMenu = MainHeader(driver, host)

    def open(self):
        self.driver.get(self.url)
        return self

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def refresh(self):
        self.driver.refresh()
        return self

    def customer_auth(self, user: User):
        self.driver.get(f"{self.host}/#/login")
        self.find_element(StartPageLocators.CUSTOMER_LOGIN_BUTTON).click()
        self.find_element(LoginPageLocators.USER_SELECTOR).click()
        self.find_element(LoginPageLocators.USER_OPTION(user.user_id)).click()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(self.driver, 5).until(ec.url_changes(f"{self.host}/#/account"))
        return self

