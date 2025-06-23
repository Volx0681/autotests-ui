import pytest
from playwright.sync_api import Page
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


def test_successful_registration(page: Page):
    reg_page = RegistrationPage(page)
    dashboard_page = DashboardPage(page)

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    reg_page.fill_form("test@example.com", "password123", "testuser")
    reg_page.submit()
    dashboard_page.verify_title()