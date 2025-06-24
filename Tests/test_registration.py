import pytest
from playwright.sync_api import Page
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

@pytest.mark.courses
@pytest.mark.registration
def test_successful_registration(page: Page, registration_page: RegistrationPage, dashboard_page: DashboardPage):
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_page.fill_registration_form_inputs("test@example.com", "password123", "testuser")
    registration_page.click_registration_form_button()

    dashboard_page.verify_dashboard_title_visible()
