from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_successful_registration():
    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        registration_email_input = page.locator('[data-testid="registration-form-email-input"] input')
        registration_password_input = page.locator('[data-testid="registration-form-password-input"] input')
        registration_username_input = page.locator('[data-testid="registration-form-username-input"] input')

        registration_email_input.fill('user.name@gmail.com')
        registration_username_input.fill('username')
        registration_password_input.fill('password')

        registration_button = page.locator('button:has-text("Registration")')
        registration_button.click()

        page.wait_for_url('**/#/dashboard')

        context.storage_state(path="browser-state.json")
        browser.close()

        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        page.wait_for_load_state("domcontentloaded")

        courses_heading = page.locator('[data-testid="courses-list-toolbar-title-text"]')
        expect(courses_heading).to_be_visible()

        no_results_heading = page.locator('[data-testid="courses-list-empty-view-title-text"]')
        expect(no_results_heading).to_be_visible()

        browser.close()
