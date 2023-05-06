import allure
from UI.PageObject.Pages.account_page import AccountPage


@allure.parent_suite("Тестовое задание")
@allure.suite("XYZ Bank. Функционал клиента")
@allure.sub_suite("Транзакции")
class TestTransactions:
    @allure.title('E2E Работа с транзакциями - пополнение, снятие, отчет')
    def test_e2e_deposit_withdraw_report(self, driver, front_host, user):
        with allure.step(f'Авторизуемся за пользователя {user}'):
            page = AccountPage(driver, front_host)
            page.customer_auth(user)
        with allure.step(f'Проверяем что отрылась страница аккаунта, видим текст "Welcome {user.username} !!"'):
            page.welcome_name_check(user.username)


