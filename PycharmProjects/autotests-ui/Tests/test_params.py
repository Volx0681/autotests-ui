import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0

@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected

@pytest.mark.parametrize("os", ["Linux", "Macos", "Windows", "debian"])
@pytest.mark.parametrize("browser", ["chromium", "webkit", "firefox"])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0

@pytest.fixture(params=["chromium", "webkit", "firefox"])
def browser(request):
    return request.param

def test_open_browser(browser: str):
    print("running open_browser: {browser}")

class TestOperations:

    @pytest.mark.parametrize("account", ["credit card", "debit card"])
    def test_user_withoperations(self, user: str, account: str):
        print("running test_user_withoperations")

    def test_user_withoutoperations(self, user: str):
        print("running test_user_withoutoperations")


users = {
    "+74951385921": "rich user",
    "+78163254496": "poor user",
    "+75132585698": "user withoperations",
}

@pytest.mark.parametrize(
    "callnumber",
    ["+74951385921", "+78163254496", "+75132585698"],
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"
)
def test_identifiers(callnumber: str):
    pass
