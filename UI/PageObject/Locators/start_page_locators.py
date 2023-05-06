from selenium.webdriver.common.by import By


class StartPageLocators:
    CUSTOMER_LOGIN_BUTTON = (By.CSS_SELECTOR, '[ng-click="customer()"]')
    BANK_MANAGER_LOGIN_BUTTON = (By.CSS_SELECTOR, '[ng-click="manager()"]')

