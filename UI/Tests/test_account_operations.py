import time
import allure
from Source.public_functions import get_today_fibonacci_num, get_now_datetime
from UI.PageObject.Pages.account_page import AccountPage
from UI.PageObject.Pages.transactions_page import TransactionsPage
from UI.Tests.public_function import create_transaction_csv_report_str, transaction_info_comparison


@allure.parent_suite("Тестовое задание")
@allure.suite("XYZ Bank. Функционал клиента")
@allure.sub_suite("Транзакции")
class TestAccountOperations:
    @allure.title('E2E Работа с транзакциями - пополнение, списание, отчет')
    def test_e2e_deposit_withdrawl_transactions(self, driver, front_host, user):
        with allure.step(f'Авторизуемся за пользователя {user.name}'):
            page = AccountPage(driver, front_host)
            page.customer_auth(user)
        with allure.step(f'Проверяем что отрылась страница аккаунта, видно текст "Welcome {user.name} !!", '
                         f'текущий баланс равен нулю'):
            page.welcome_name_check(user.name)
            balance = page.get_balance_value()
            assert balance == 0, "Текущий баланс не 0"

        amount = get_today_fibonacci_num()
        with allure.step(f'Пополняем счет на сумму числа Фибоначчи: {amount}'):
            page.deposit(amount)
            deposit_datetime = get_now_datetime()
            time.sleep(1)  # время чтобы "бэк" успел отработать
        with allure.step(f'Списываем со счета сумму числа Фибоначчи: {amount}'):
            page.withdrawl(amount)
            withdrawl_datetime = get_now_datetime()
            time.sleep(1)  # время чтобы "бэк" успел отработать
        with allure.step(f'Проверяем что текущий баланс равен нулю'):
            balance = page.get_balance_value()
            assert balance == 0, "Текущий баланс не 0"

        with allure.step(f'Переходим на страницу транзакций, собираем данные о транзакциях'):
            page.go_to_transactions()
            page = TransactionsPage(driver, front_host)
            deposit_tr_info = page.get_transaction_info(transaction_id=0)
            withdrawl_tr_info = page.get_transaction_info(transaction_id=1)

        # Формируем отчет о транзакциях в csv
        report_str = create_transaction_csv_report_str([deposit_tr_info, withdrawl_tr_info])
        allure.attach(report_str, name='transaction_report', attachment_type=allure.attachment_type.CSV)

        with allure.step(f'Проверяем соответствие времени, суммы и типа транзакции пополнения'):
            expected_deposit_info = {
                'Date-Time': deposit_datetime,
                'Amount': str(amount),
                'Transaction Type': "Credit"
            }
            transaction_info_comparison(deposit_tr_info, expected_deposit_info)
        with allure.step(f'Проверяем соответствие времени, суммы и типа транзакции списания'):
            expected_withdrawl_info = {
                'Date-Time': withdrawl_datetime,
                'Amount': str(amount),
                'Transaction Type': "Debit"
            }
            transaction_info_comparison(withdrawl_tr_info, expected_withdrawl_info)

