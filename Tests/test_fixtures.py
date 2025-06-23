from playwright.sync_api import expect, Page
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_heading = page.locator('[data-testid="courses-list-toolbar-title-text"]')
    no_results_heading = page.locator('[data-testid="courses-list-empty-view-title-text"]')

    expect(courses_heading).to_be_visible()
    expect(no_results_heading).to_be_visible()
