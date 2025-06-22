import pytest
from playwright.sync_api import Playwright, Page


def pytest_configure(config):
    config.addinivalue_line("markers", "courses: тесты для работы с курсами")
    config.addinivalue_line("markers", "regression: регрессионные тесты")
    config.addinivalue_line("markers", "smoke: смок тесты")
    config.addinivalue_line("markers", "api: тесты API")
    config.addinivalue_line("markers", "ui: UI-тесты")
    config.addinivalue_line("markers", "critical: критические тесты")
    config.addinivalue_line("markers", "auth: тесты авторизации")
    config.addinivalue_line("markers", "slow: медленные тесты")

@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    browser.close()

