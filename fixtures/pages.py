import pytest
from playwright.sync_api import Page
from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage
from pages.dashboard_page import DashboardPage


@pytest.fixture
def create_course_page(chromium_page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(chromium_page_with_state)


@pytest.fixture
def courses_list_page(chromium_page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(chromium_page_with_state)


@pytest.fixture
def course_image_file() -> str:
    return "testdata/files/image.png"


@pytest.fixture
def dashboard_page_with_state(chromium_page_with_state: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page_with_state)