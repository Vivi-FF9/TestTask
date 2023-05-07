import allure
import pytest
from Source.users import HarryPotter


@pytest.fixture(scope='session')
@allure.title("Пользователь")
def user():
    user = HarryPotter
    allure.attach(str(user.__dict__), user.name)
    return user

