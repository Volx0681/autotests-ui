import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] отправляет аналитику")

@pytest.fixture(scope="session")
def settings():
    print("[SESSION] включаем автотесты")
@pytest.fixture(scope="class")
def user():
    print("[CLASS] создаём юзера")

@pytest.fixture(scope="function")
def browser():
    print("[FUNCTION] раздупляем браузер")


class TestUserFlow:
    def test_user_can_login(self, settings):
        ...

    def test_user_create_course(self, settings,user,browser):
        ...

    def test_user_account(self, settings,user,browser):
        ...