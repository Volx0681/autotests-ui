from playwright.sync_api import Page, expect

class DashboardToolbarViewComponent:
    def __init__(self, page: Page):
        self.title = page.get_by_test_id('dashboard-toolbar-title-text')

    def check_visible(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Dashboard')