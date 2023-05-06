from UI.PageObject.Pages.base_page import BasePage


class AccountPage(BasePage):
    def __init__(self, driver, host):
        super().__init__(driver, host)
        self.url = f"{self.host}/#/account"

    def welcome_name_check(self, name: str):
        pass

    def balance_check(self):
        pass

    def withdraw(self, amount: int):
        pass

    def deposit(self, amount: int):
        pass

    def go_to_transactions(self):
        pass

