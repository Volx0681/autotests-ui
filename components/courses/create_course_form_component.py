from playwright.sync_api import Page, expect

class CreateCourseFormComponent:
    def __init__(self, page: Page):
        self.title_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.time_input = page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        self.description_input = page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        self.max_score_input = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.min_score_input = page.get_by_test_id('create-course-form-min-score-input').locator('input')

    def fill(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title_input.fill(title)
        self.time_input.fill(estimated_time)
        self.description_input.fill(description)
        self.max_score_input.fill(max_score)
        self.min_score_input.fill(min_score)
        expect(self.title_input).to_have_value(title)
        expect(self.time_input).to_have_value(estimated_time)
        expect(self.description_input).to_have_value(description)
        expect(self.max_score_input).to_have_value(max_score)
        expect(self.min_score_input).to_have_value(min_score)

    def check_visible(self,
                      title: str = None,
                      estimated_time: str = None,
                      description: str = None,
                      max_score: str = None,
                      min_score: str = None):
        expect(self.title_input).to_be_visible()
        expect(self.time_input).to_be_visible()
        expect(self.description_input).to_be_visible()
        expect(self.max_score_input).to_be_visible()
        expect(self.min_score_input).to_be_visible()

        if title is not None:
            expect(self.title_input).to_have_value(title)
        if estimated_time is not None:
            expect(self.time_input).to_have_value(estimated_time)
        if description is not None:
            expect(self.description_input).to_have_value(description)
        if max_score is not None:
            expect(self.max_score_input).to_have_value(max_score)
        if min_score is not None:
            expect(self.min_score_input).to_have_value(min_score)
