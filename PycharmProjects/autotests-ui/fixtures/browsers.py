import pytest
from playwright.sync_api import Playwright, sync_playwright, Page

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