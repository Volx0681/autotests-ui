import pytest
@pytest.mark.smoke
def some_case():
    ...


@pytest.mark.regression
def test_regression_case():
    ...


class TestSuite:
    @pytest.mark.marked
    def testcase1(selfself):
        ...
    def testcase2(self):
        ...

@pytest.mark.regression
class TestUserAuthentication:
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login(self):
        ...
    @pytest.mark.slow
    def password_reset(self):
        ...
    def user_logout(self):
        ...