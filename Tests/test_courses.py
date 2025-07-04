import pytest
from pathlib import Path
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage

@pytest.mark.courses
@pytest.mark.regression
def test_create_course(chromium_page_with_state, course_image_file):

    courses_list_page = CoursesListPage(chromium_page_with_state)
    create_course_page = CreateCoursePage(chromium_page_with_state)

    create_course_page.visit(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create"
    )
    chromium_page_with_state.wait_for_load_state("networkidle")

    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form(
        title="", estimated_time="", description="", max_score="0", min_score="0"
    )

    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()

    create_course_page.click_create_exercise_button()
    create_course_page.check_visible_create_exercise_form(
        index=0,
        title="Exercise title",
        description="Exercise description"
    )

    create_course_page.upload_preview_image(course_image_file)
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)

    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )
    create_course_page.click_create_course_button()

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        index=0,
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks"
    )
