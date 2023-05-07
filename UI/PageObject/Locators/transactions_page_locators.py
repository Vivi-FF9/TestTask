from selenium.webdriver.common.by import By


class TransactionPageLocators:
    BACK_BUTTON = (By.CSS_SELECTOR, '[ng-click="back()"]')
    RESET_BUTTON = (By.CSS_SELECTOR, '[ng-click="reset()"]')

    @staticmethod
    def TRANSACTION_INFO_ELEMENTS(transaction_id):
        return By.CSS_SELECTOR, f'#anchor{transaction_id} .ng-binding'

