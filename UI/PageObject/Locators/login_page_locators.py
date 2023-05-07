from selenium.webdriver.common.by import By


class LoginPageLocators:
    USER_SELECTOR = (By.CSS_SELECTOR, '#userSelect')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

    @staticmethod
    def USER_OPTION(customer_id):
        return By.CSS_SELECTOR, f'[value="{customer_id}"]'

