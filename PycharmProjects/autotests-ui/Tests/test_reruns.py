from playwright.sync_api import expect, Page
import pytest
import random

@pytest.mark.flaky(reruns=2, reruns_delay=5)
@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    assert random.choice({True, False})

    page = chromium_page_with_state

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_heading = page.locator('[data-testid="courses-list-toolbar-title-text"]')
    no_results_heading = page.locator('[data-testid="courses-list-empty-view-title-text"]')

    expect(courses_heading).to_be_visible()
    expect(no_results_heading).to_be_visible()


class TestReruns:

    def test_rerun1(self):
        assert random.choice({True, False})

    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_rerun2(self):
        assert random.choice({True, False})