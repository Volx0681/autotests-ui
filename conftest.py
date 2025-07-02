# conftest.py

import pytest
from pathlib import Path
from playwright.sync_api import Playwright, Page
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage

# Фикстура для запуска браузера
@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    browser.close()

# Инициализация состояния браузера (сессия для зарегистрированного пользователя)
@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # выполняем регистрацию стандартным пользователем
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    page.locator('[data-testid="registration-form-email-input"] input').fill('user.name@gmail.com')
    page.locator('[data-testid="registration-form-username-input"] input').fill('username')
    page.locator('[data-testid="registration-form-password-input"] input').fill('password')
    page.locator('button:has-text("Registration")').click()
    page.wait_for_url("**/#/dashboard")
    context.storage_state(path="browser-state.json")
    browser.close()

# Фикстура для страницы с сохранённым состоянием
@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()
    yield page
    browser.close()

# Фикстуры страниц
@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    registration = RegistrationPage(chromium_page)
    registration.visit(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    )
    return registration

@pytest.fixture
def dashboard_page(chromium_page_with_state: Page) -> DashboardPage:
    dashboard = DashboardPage(chromium_page_with_state)
    dashboard.visit(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard"
    )
    return dashboard

@pytest.fixture
def courses_list_page(chromium_page_with_state: Page) -> CoursesListPage:
    courses = CoursesListPage(chromium_page_with_state)
    courses.visit(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
    )
    return courses

@pytest.fixture
def create_course_page(chromium_page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(chromium_page_with_state)

@pytest.fixture
def course_image_file():
    return str(Path(__file__).parent / "testdata" / "files" / "image.png")