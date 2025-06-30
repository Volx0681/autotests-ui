from playwright.sync_api import Page, expect
from typing import Tuple


class SidebarComponent:
    def __init__(self, page: Page):
        self.page = page

        self._sidebar = page.get_by_test_id('sidebar')
        self._dashboard_link = page.get_by_test_id('sidebar-dashboard-link')

        self._mobile_toggle = page.get_by_test_id('sidebar-mobile-toggle')

    def check_visible_sidebar(self, check_links: bool = True) -> Tuple[bool, str]:

        error_messages = []

        try:
            expect(self._sidebar).to_be_visible(timeout=7000)
        except Exception as e:
            error_messages.append(f"Sidebar container not visible: {str(e)}")

        if check_links:
            try:
                expect(self._dashboard_link).to_be_visible(timeout=3000)
            except Exception as e:
                error_messages.append(f"Dashboard link not found: {str(e)}")

            try:
                expect(self._courses_link).to_be_visible(timeout=3000)
            except Exception as e:
                error_messages.append(f"Courses link not found: {str(e)}")

        if error_messages:
            return False, " | ".join(error_messages)
        return True,

    def is_sidebar_open(self) -> bool:

        try:
            return self._sidebar.is_visible()
        except:
            return False

    def toggle_mobile_sidebar(self):

        self._mobile_toggle.click()
        self.page.wait_for_timeout(500)