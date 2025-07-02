# pages/login_page.py

from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from components.authentication.login_form_component import LoginFormComponent

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.form = LoginFormComponent(page)
        self.wrong_email_or_password_alert = page.get_by_test_id(
            'login-page-wrong-email-or-password-alert'
        )

    def fill_login_form(self, email: str, password: str):
        self.form.fill(email, password)

    def check_visible_login_form(self, email: str = None, password: str = None):
        self.form.check_visible(email, password)

    def click_login_button(self):
        self.form.submit_button.click()
        self.page.wait_for_load_state("networkidle")

    def check_visible_wrong_email_or_password_alert(self):
        expect(self.wrong_email_or_password_alert).to_be_visible()
        expect(self.wrong_email_or_password_alert).to_have_text(
            "Wrong email or password"
        )
