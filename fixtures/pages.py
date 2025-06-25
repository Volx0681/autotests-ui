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

@pytest.fixture(scope='function')
def courses_list_page(chromium_page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(page=chromium_page_with_state)

@pytest.fixture
def create_course_page(chromium_page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(page=chromium_page_with_state)