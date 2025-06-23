from playwright.sync_api import Page, expect

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator('[data-testid="dashboard-toolbar-title-text"]')

    def verify_title(self):
        expect(self.title).to_have_text("Dashboard")