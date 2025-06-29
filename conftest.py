import pytest
from pathlib import Path
from playwright.sync_api import Playwright, Page

pytest_plugins = [
    "fixtures.pages"
]

def pytest_configure(config):
    config.addinivalue_line("markers", "courses: тесты для работы с курсами")
    config.addinivalue_line("markers", "regression: регрессионные тесты")
    config.addinivalue_line("markers", "smoke: смок тесты")
    config.addinivalue_line("markers", "api: тесты API")
    config.addinivalue_line("markers", "ui: UI-тесты")
    config.addinivalue_line("markers", "critical: критические тесты")
    config.addinivalue_line("markers", "authorization: тесты авторизации")
    config.addinivalue_line("markers", "slow: медленные тесты")

@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    browser.close()

@pytest.fixture(scope="session")
def initialize_browser_state(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    email_input = page.locator('[data-testid="registration-form-email-input"] input')
    username_input = page.locator('[data-testid="registration-form-username-input"] input')
    password_input = page.locator('[data-testid="registration-form-password-input"] input')
    register_button = page.locator('button:has-text("Registration")')
    email_input.fill('user.name@gmail.com')
    username_input.fill('username')
    password_input.fill('password')
    register_button.click()
    page.wait_for_url('**/#/dashboard')
    context.storage_state(path="browser-state.json")
    browser.close()

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()
    yield page
    browser.close()

@pytest.fixture
def course_image_file():
    return str(Path(__file__).parent / "testdata" / "files" / "image.png")

@pytest.fixture
def dashboard_page(chromium_page_with_state):
    dashboard = DashboardPage(chromium_page_with_state)
    dashboard.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    return dashboard

@pytest.fixture
def courses_list_page(chromium_page_with_state):
    courses = CoursesListPage(chromium_page_with_state)
    courses.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    return courses

@pytest.fixture
def create_course_page(chromium_page_with_state):
    return CreateCoursePage(chromium_page_with_state)