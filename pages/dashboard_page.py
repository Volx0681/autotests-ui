from playwright.sync_api import Page, expect

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')

    def verify_dashboard_title_visible(self):
        expect(self.dashboard_title).to_be_visible()