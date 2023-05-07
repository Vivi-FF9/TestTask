from selenium.webdriver.common.by import By


class AccountPageLocators:
    WELCOME_NAME = (By.CSS_SELECTOR, '.fontBig.ng-binding')
    TRANSACTIONS_BUTTON = (By.CSS_SELECTOR, '[ng-click="transactions()"]')
    WITHDRAWL_BUTTON = (By.CSS_SELECTOR, '[ng-click="withdrawl()"]')
    DEPOSIT_BUTTON = (By.CSS_SELECTOR, '[ng-click="deposit()"]')
    AMOUNT_INPUT = (By.CSS_SELECTOR, 'input[type="number"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    ACCOUNT_INFO_ELEMENTS = (By.CSS_SELECTOR, '.center .ng-binding')
    MESSAGE = (By.CSS_SELECTOR, '[ng-show="message"]')
