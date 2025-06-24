import pytest
from playwright.sync_api import Page
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

@pytest.fixture(scope='function')
def registration_page(page: Page) -> RegistrationPage:
    return RegistrationPage(page)

@pytest.fixture(scope='function')
def dashboard_page(page: Page) -> DashboardPage:
    return DashboardPage(page)
