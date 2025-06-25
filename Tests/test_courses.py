import pytest
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(chromium_page_with_state, course_image_file):
    # Initialize page objects
    courses_list_page = CoursesListPage(chromium_page_with_state)
    create_course_page = CreateCoursePage(chromium_page_with_state)

    # Step 1: Open the create course page
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    chromium_page_with_state.wait_for_load_state("networkidle")

    # Debug: Print current URL and page content
    print(f"Current URL: {chromium_page_with_state.url}")
    print(f"Page title: {chromium_page_with_state.title()}")

    # Step 2: Check create course title
    create_course_page.check_visible_create_course_title()

    # Step 3: Check create course button is disabled
    create_course_page.check_disabled_create_course_button()

    # Step 4: Check empty preview image block
    create_course_page.check_visible_image_preview_empty_view()

    # Step 5: Check image upload view in default state
    create_course_page.check_visible_image_upload_view()

    # Debug: Verify the upload input is present
    upload_input = chromium_page_with_state.get_by_test_id("create-course-preview-image-upload-widget-input")
    print(f"Upload input visible: {upload_input.is_visible()}")
    print(f"Upload input count: {upload_input.count()}")

    # Step 6: Check create course form with default values
    create_course_page.check_visible_create_course_form(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0"
    )

    # Step 7: Check exercises title
    create_course_page.check_visible_exercises_title()

    # Step 8: Check create exercise button
    create_course_page.check_visible_create_exercise_button()

    # Step 9: Check empty exercises view
    create_course_page.check_visible_exercises_empty_view()

    # Debug: Print the image file path
    print(f"Image file path: {course_image_file}")
    print(f"File exists: {Path(course_image_file).exists()}")

    # Step 10: Upload preview image with longer timeout
    upload_input = chromium_page_with_state.get_by_test_id("create-course-preview-image-upload-widget-input")
    upload_input.set_input_files(course_image_file, timeout=60000)

    # Step 11: Check image upload view with uploaded image
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)

    # Step 12: Fill create course form
    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )

    # Step 13: Click create course button
    create_course_page.click_create_course_button()

    # Step 14: Check courses list page title
    courses_list_page.check_visible_courses_title()

    # Step 15: Check create course button is visible
    courses_list_page.check_visible_create_course_button()

    # Step 16: Check course card with expected values
    courses_list_page.check_visible_course_card(
        index=0,
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks"
    )