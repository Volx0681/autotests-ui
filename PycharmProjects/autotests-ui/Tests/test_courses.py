from playwright.sync_api import expect
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list_old(chromium_page):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = chromium_page.locator('[data-testid="registration-form-email-input"] input')
    username_input = chromium_page.locator('[data-testid="registration-form-username-input"] input')
    password_input = chromium_page.locator('[data-testid="registration-form-password-input"] input')
    register_button = chromium_page.locator('button:has-text("Registration")')

    email_input.fill('user.name@gmail.com')
    username_input.fill('username')
    password_input.fill('password')
    register_button.click()

    chromium_page.wait_for_url('**/#/dashboard')

    chromium_page.context.storage_state(path="browser-state.json")
    chromium_page.close()
    chromium_page = chromium_page.context.browser.new_page(storage_state="browser-state.json")

    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    chromium_page.wait_for_load_state("domcontentloaded")

    courses_heading = chromium_page.locator('[data-testid="courses-list-toolbar-title-text"]')
    no_results_heading = chromium_page.locator('[data-testid="courses-list-empty-view-title-text"]')

    expect(courses_heading).to_be_visible()
    expect(no_results_heading).to_be_visible()
    chromium_page.close()