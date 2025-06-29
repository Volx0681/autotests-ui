import pytest
from playwright.sync_api import Page
from pages.courses_list_page import CoursesListPage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    page = CoursesListPage(chromium_page_with_state)
    page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    page.navbar.check_visible_navbar(check_profile_button=False)

    page.sidebar.check_visible_sidebar()

    page.check_visible_courses_title()

    page.check_visible_create_course_button()

    page.check_visible_empty_view()
