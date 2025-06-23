from playwright.sync_api import Page

class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator('[data-testid="registration-form-email-input"] input')
        self.password_input = page.locator('[data-testid="registration-form-password-input"] input')
        self.username_input = page.locator('[data-testid="registration-form-username-input"] input')
        self.register_button = page.locator('button:has-text("Registration")')

    def fill_form(self, email: str, password: str, username: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.username_input.fill(username)

    def submit(self):
        self.register_button.click()