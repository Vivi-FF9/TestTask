from UI.PageObject.Pages.base_page import BasePage
from UI.PageObject.Locators.transactions_page_locators import TransactionPageLocators
from Source.public_functions import str_to_datetime_object


class TransactionsPage(BasePage):
    def __init__(self, driver, host):
        super().__init__(driver, host)
        self.url = f"{self.host}/#/listTx"

    def get_transaction_info(self, transaction_id: int) -> dict:
        transaction_info = self.find_elements(TransactionPageLocators.TRANSACTION_INFO_ELEMENTS(transaction_id))
        result = {
            'Date-Time': str_to_datetime_object(transaction_info[0].text),
            'Amount': transaction_info[1].text,
            'Transaction Type': transaction_info[2].text
        }
        return result

