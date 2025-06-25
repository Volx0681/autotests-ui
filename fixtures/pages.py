import pytest
from playwright.sync_api import Page
from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage


@pytest.fixture
def create_course_page(chromium_page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(chromium_page_with_state)


@pytest.fixture
def courses_list_page(chromium_page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(chromium_page_with_state)

@pytest.fixture
def course_image_file() -> str:
    return "testdata/files/image.png"