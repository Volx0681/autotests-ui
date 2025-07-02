from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent

class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')

        self.preview_image = page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')
        self.preview_empty_view_icon = page.get_by_test_id('create-course-preview-empty-view-icon')
        self.preview_empty_view_title = page.get_by_test_id('create-course-preview-empty-view-title-text')
        self.preview_empty_view_description = page.get_by_test_id('create-course-preview-empty-view-description-text')

        self.preview_image_upload_icon = page.get_by_test_id('create-course-preview-image-upload-widget-info-icon')
        self.preview_image_upload_title = page.get_by_test_id('create-course-preview-image-upload-widget-info-title-text')
        self.preview_image_upload_description = page.get_by_test_id('create-course-preview-image-upload-widget-info-description-text')
        self.preview_image_upload_button = page.get_by_test_id('create-course-preview-image-upload-widget-upload-button')
        self.preview_image_remove_button = page.get_by_test_id('create-course-preview-image-upload-widget-remove-button')
        self.preview_image_upload_input = page.get_by_test_id('create-course-preview-image-upload-widget-input')

        self.create_course_title_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.create_course_estimated_time_input = page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        self.create_course_description_textarea = page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        self.create_course_max_score_input = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.create_course_min_score_input = page.get_by_test_id('create-course-form-min-score-input').locator('input')

        self.exercises = CreateCourseExercisesToolbarViewComponent(page)

        self.exercises_empty_view_icon = page.get_by_test_id('create-course-exercises-empty-view-icon')
        self.exercises_empty_view_title = page.get_by_test_id('create-course-exercises-empty-view-title-text')
        self.exercises_empty_view_description = page.get_by_test_id('create-course-exercises-empty-view-description-text')

    def check_visible_create_course_title(self):
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text('Create course')

    def click_create_course_button(self):
        self.create_course_button.click()

    def check_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def check_disabled_create_course_button(self):
        expect(self.create_course_button).to_be_disabled()

    def check_visible_image_preview_empty_view(self):
        expect(self.preview_empty_view_icon).to_be_visible()
        expect(self.preview_empty_view_title).to_be_visible()
        expect(self.preview_empty_view_title).to_have_text('No image selected')
        expect(self.preview_empty_view_description).to_be_visible()
        expect(self.preview_empty_view_description).to_have_text('Preview of selected image will be displayed here')

    def check_visible_image_upload_view(self, is_image_uploaded: bool = False):
        expect(self.preview_image_upload_icon).to_be_visible()
        expect(self.preview_image_upload_title).to_be_visible()
        expect(self.preview_image_upload_title).to_have_text('Tap on "Upload image" button to select file')
        expect(self.preview_image_upload_description).to_be_visible()
        expect(self.preview_image_upload_description).to_have_text('Recommended file size 540X300')
        expect(self.preview_image_upload_button).to_be_visible()
        if is_image_uploaded:
            expect(self.preview_image_remove_button).to_be_visible()

    def upload_preview_image(self, file: str):
        self.preview_image_upload_input.set_input_files(file)

    def click_remove_image_button(self):
        self.preview_image_remove_button.click()

    def check_visible_preview_image(self):
        expect(self.preview_image).to_be_visible()

    def check_visible_create_course_form(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        expect(self.create_course_title_input).to_be_visible()
        expect(self.create_course_title_input).to_have_value(title)
        expect(self.create_course_estimated_time_input).to_be_visible()
        expect(self.create_course_estimated_time_input).to_have_value(estimated_time)
        expect(self.create_course_description_textarea).to_be_visible()
        expect(self.create_course_description_textarea).to_have_value(description)
        expect(self.create_course_max_score_input).to_be_visible()
        expect(self.create_course_max_score_input).to_have_value(max_score)
        expect(self.create_course_min_score_input).to_be_visible()
        expect(self.create_course_min_score_input).to_have_value(min_score)

    def fill_create_course_form(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.create_course_title_input.fill(title)
        expect(self.create_course_title_input).to_have_value(title)
        self.create_course_estimated_time_input.fill(estimated_time)
        expect(self.create_course_estimated_time_input).to_have_value(estimated_time)
        self.create_course_description_textarea.fill(description)
        expect(self.create_course_description_textarea).to_have_value(description)
        self.create_course_max_score_input.fill(max_score)
        expect(self.create_course_max_score_input).to_have_value(max_score)
        self.create_course_min_score_input.fill(min_score)
        expect(self.create_course_min_score_input).to_have_value(min_score)

    def check_visible_exercises_title(self):
        self.exercises.check_visible()

    def check_visible_create_exercise_button(self):
        self.exercises.check_visible_button()

    def click_create_exercise_button(self):
        self.exercises.click()

    def check_visible_exercises_empty_view(self):
        expect(self.exercises_empty_view_icon).to_be_visible()
        expect(self.exercises_empty_view_title).to_be_visible()
        expect(self.exercises_empty_view_title).to_have_text('There is no exercises')
        expect(self.exercises_empty_view_description).to_be_visible()
        expect(self.exercises_empty_view_description).to_have_text('Click on "Create exercise" button to create new exercise')

    def check_visible_create_exercise_form(self, index: int, title: str, description: str):
        subtitle = self.page.get_by_test_id(f"create-course-exercise-{index}-box-toolbar-subtitle-text")
        title_input = self.page.get_by_test_id(f"create-course-exercise-form-title-{index}-input").locator('input')
        desc_input = self.page.get_by_test_id(f"create-course-exercise-form-description-{index}-input").locator('input')
        expect(subtitle).to_be_visible()
        expect(subtitle).to_have_text(f"#{index + 1} Exercise")
        expect(title_input).to_be_visible()
        expect(title_input).to_have_value(title)
        expect(desc_input).to_be_visible()
        expect(desc_input).to_have_value(description)

    def fill_create_exercise_form(self, index: int, title: str, description: str):
        title_input = self.page.get_by_test_id(f"create-course-exercise-form-title-{index}-input").locator('input')
        desc_input = self.page.get_by_test_id(f"create-course-exercise-form-description-{index}-input").locator('input')
        title_input.fill(title)
        expect(title_input).to_have_value(title)
        desc_input.fill(description)
        expect(desc_input).to_have_value(description)
