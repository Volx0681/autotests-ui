from playwright.sync_api import Page
from .base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.registration_form = RegistrationFormComponent(page)

    def visit(self, url: str):
        self.page.goto(url)

    def fill_registration_form_inputs(self, email: str, password: str, username: str):
        self.registration_form.fill(email, username, password)

    def click_registration_form_button(self):
        self.registration_form.submit_button.click()
