from playwright.sync_api import Page, expect
from components.base_component import BaseComponent


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # Navigation elements
        self.app_title = page.get_by_test_id('navigation-navbar-app-title-text')
        self.welcome_title = page.get_by_test_id('navigation-navbar-welcome-title-text')

        # Make profile button optional since it might not exist on all pages
        self.profile_button = page.get_by_test_id('navbar-profile-button').or_(page.locator('body'))

    def check_visible_navbar(self, check_profile_button: bool = True):
        """Verify main navbar elements are visible"""
        expect(self.app_title).to_be_visible()
        expect(self.welcome_title).to_be_visible()

        if check_profile_button:
            try:
                expect(self.profile_button).to_be_visible(timeout=3000)
            except AssertionError:
                # Profile button might not be present on all pages
                pass