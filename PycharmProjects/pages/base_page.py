from playwright.sync_api import page

class BasePage:
    def __init__(self, page):
        self.page = page

    def visit(self, url: str):
        self.page.goto(url , waitUntil='networkidle')

    def reload(self):
        self.page.reload(waitUntil='networkidle')