import allure
from UI.PageObject.Pages.account_page import AccountPage
from Source.public_functions import get_today_fibonacci_num


@allure.parent_suite("Тестовое задание")
@allure.suite("XYZ Bank. Функционал клиента")
@allure.sub_suite("Транзакции")
class TestAccountOperations:
    @allure.title('E2E Работа с транзакциями - пополнение, списание, отчет')
    def test_e2e_deposit_withdrawl_transactions(self, driver, front_host, user):
        with allure.step(f'Авторизуемся за пользователя {user}'):
            page = AccountPage(driver, front_host)
            page.customer_auth(user)
        with allure.step(f'Проверяем что отрылась страница аккаунта, видно текст "Welcome {user.username} !!",'
                         f'текущий баланс равен нулю'):
            page.welcome_name_check(user.username)
            balance = page.get_balance_value()
            assert balance == 0

        amount = get_today_fibonacci_num()
        with allure.step(f'Пополняем счет на сумму числа Фибоначчи: {amount}'):
            page.deposit(amount)
        with allure.step(f'Списываем со счета сумму числа Фибоначчи: {amount}'):
            page.withdrawl(amount)
        with allure.step(f'Проверяем что текущий баланс равен нулю'):
            balance = page.get_balance_value()
            assert balance == 0
