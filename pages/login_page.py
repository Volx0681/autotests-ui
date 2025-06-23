from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_input = page.get_by_test_id('login-form-password-input').locator('input')
        self.login_button = page.get_by_test_id('login-page-login-button')
        self.wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')

    def fill_login_form(self, email: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)
        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_login_button(self):
        expect(self.login_button).to_be_visible()
        expect(self.login_button).to_be_enabled()
        self.login_button.click()
        self.page.wait_for_load_state("networkidle")

    def check_visible_wrong_email_or_password_alert(self):
        expect(self.wrong_email_or_password_alert).to_be_visible
        expect(self.wrong_email_or_password_alert).to_have_text("Wrong email or password")