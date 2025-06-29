import pytest
from playwright.sync_api import Page
from pages.courses_list_page import CoursesListPage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    page = CoursesListPage(chromium_page_with_state)
    page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # 1. Проверка Navbar
    page.navbar.check_visible_navbar(check_profile_button=False)

    # 2. Проверка Sidebar
    page.sidebar.check_visible_sidebar()

    # 3. Проверка заголовка "Courses"
    page.check_visible_courses_title()

    # 4. Проверка кнопки создания курса
    page.check_visible_create_course_button()

    # 5. Проверка пустого блока
    page.check_visible_empty_view()
