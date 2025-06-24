from playwright.sync_api import Page

class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.input_registration_form_email = page.locator('[data-testid="registration-form-email-input"] input')
        self.input_registration_form_password = page.locator('[data-testid="registration-form-password-input"] input')
        self.input_registration_form_username = page.locator('[data-testid="registration-form-username-input"] input')
        self.button_registration_form_submit = page.locator('button:has-text("Registration")')

    def fill_registration_form_inputs(self, email: str, password: str, username: str):
        self.input_registration_form_email.fill(email)
        self.input_registration_form_password.fill(password)
        self.input_registration_form_username.fill(username)

    def click_registration_form_button(self):
        self.button_registration_form_submit.click()