from selenium.webdriver.remote.webdriver import WebDriver
from Source.users import User
from UI.PageObject.Pages.abstract_page import AbsPage
from UI.PageObject.Locators.main_header_locators import MainHeaderLocators
from UI.PageObject.Locators.start_page_locators import StartPageLocators
from UI.PageObject.Locators.login_locators import LoginPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class MainHeader(AbsPage):
    def __init__(self, driver: WebDriver, host: str):
        super().__init__(driver, host)

    def go_home(self):
        self.find_element(MainHeaderLocators.HOME_BUTTON).click()

    def logout(self):
        self.find_element(MainHeaderLocators.LOGOUT_BUTTON).click()


class BasePage(AbsPage):
    def __init__(self, driver: WebDriver, host: str):
        super().__init__(driver, host)
        self.MainHeaderMenu = MainHeader(driver, host)

    def customer_auth(self, user: User):
        self.driver.get(f"{self.host}/#/login")
        self.find_element(StartPageLocators.CUSTOMER_LOGIN_BUTTON).click()
        self.find_element(LoginPageLocators.USER_SELECTOR).click()
        self.find_element(LoginPageLocators.USER_OPTION(user.customer_id)).click()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(self.driver, 10).until(ec.url_changes(f"{self.host}/#/account"))
        return self
