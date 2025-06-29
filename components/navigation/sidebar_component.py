from playwright.sync_api import Page, expect

class SidebarComponent:
    def __init__(self, page: Page):
        self.page = page
        self.sidebar = page.get_by_test_id('sidebar')
        self.dashboard_link = page.get_by_test_id('sidebar-dashboard-link')
        self.courses_link = page.get_by_test_id('sidebar-courses-link')

    def check_visible_sidebar(self):
        expect(self.sidebar).to_be_visible()
        expect(self.dashboard_link).to_be_visible()
        expect(self.courses_link).to_be_visible()