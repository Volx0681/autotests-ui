from playwright.sync_api import Page
import pytest
from pages.dashboard_page import DashboardPage


@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard_displaying(chromium_page_with_state: Page):
    page = DashboardPage(chromium_page_with_state)
    page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    page.navbar.check_visible_navbar(check_profile_button=False)

    page.check_visible_dashboard_title()
    page.check_visible_students_chart()
    page.check_visible_courses_chart()
    page.check_visible_activities_chart()
    page.check_visible_scores_chart()
