from playwright.sync_api import Page, expect

class LoginFormComponent:
    def __init__(self, page: Page):
        self.email_input = page.locator('[data-testid="login-form-email-input"] input')
        self.password_input = page.locator('[data-testid="login-form-password-input"] input')
        self.submit_button = page.locator('button:has-text("Login")')

    def fill(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        expect(self.email_input).to_have_value(email)
        expect(self.password_input).to_have_value(password)

    def check_visible(self, email: str = None, password: str = None):
        expect(self.email_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.submit_button).to_be_visible()
        if email is not None:
            expect(self.email_input).to_have_value(email)
        if password is not None:
            expect(self.password_input).to_have_value(password)