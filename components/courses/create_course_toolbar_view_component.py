from playwright.sync_api import Page, expect

class CreateCourseToolbarViewComponent:
    def __init__(self, page: Page):
        self.create_course_button = page.locator('[data-testid="create-course-button"]')

    def check_visible(self, is_create_course_disabled: bool = True):
        expect(self.create_course_button).to_be_visible()
        if is_create_course_disabled:
            expect(self.create_course_button).to_be_disabled()
        else:
            expect(self.create_course_button).to_be_enabled()

    def click_create_course_button(self):
        self.create_course_button.click()