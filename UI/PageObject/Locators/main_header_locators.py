from selenium.webdriver.common.by import By


class MainHeaderLocators:
    HOME_BUTTON = (By.CSS_SELECTOR, '[ng-click="home()"]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '[ng-click="byebye()"]')
    MAIN_HEADING = (By.CSS_SELECTOR, '.mainHeading')
