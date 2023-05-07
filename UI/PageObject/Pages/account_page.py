from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from UI.PageObject.Pages.base_page import BasePage
from UI.PageObject.Locators.account_page_locators import AccountPageLocators


class AccountPage(BasePage):
    def __init__(self, driver, host):
        super().__init__(driver, host)
        self.url = f"{self.host}/#/account"

    def welcome_name_check(self, name: str):
        e_text = self.find_element(AccountPageLocators.WELCOME_NAME).text
        assert e_text == name

    def get_balance_value(self):
        account_info = self.find_elements(AccountPageLocators.ACCOUNT_INFO_ELEMENTS)
        balance_value = int(account_info[1].text)
        return balance_value

    def withdrawl(self, amount: int):
        self.find_element(AccountPageLocators.WITHDRAWL_BUTTON).click()
        WebDriverWait(self.driver, 3) \
            .until(ec.text_to_be_present_in_element(AccountPageLocators.SUBMIT_BUTTON, "Withdraw"))
        self.find_element(AccountPageLocators.AMOUNT_INPUT).send_keys(str(amount))
        self.find_element(AccountPageLocators.SUBMIT_BUTTON).click()
        WebDriverWait(self.driver, 5)\
            .until(ec.text_to_be_present_in_element(AccountPageLocators.MESSAGE, "Transaction successful"))

    def deposit(self, amount: int):
        self.find_element(AccountPageLocators.DEPOSIT_BUTTON).click()
        WebDriverWait(self.driver, 3) \
            .until(ec.text_to_be_present_in_element(AccountPageLocators.SUBMIT_BUTTON, "Deposit"))
        self.find_element(AccountPageLocators.AMOUNT_INPUT).send_keys(str(amount))
        self.find_element(AccountPageLocators.SUBMIT_BUTTON).click()
        WebDriverWait(self.driver, 5) \
            .until(ec.text_to_be_present_in_element(AccountPageLocators.MESSAGE, "Deposit Successful"))

    def go_to_transactions(self):
        self.find_element(AccountPageLocators.TRANSACTIONS_BUTTON).click()
        WebDriverWait(self.driver, 5).until(ec.url_changes(f"{self.host}/#/listTx"))

