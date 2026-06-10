import os
from playwright.sync_api import Page

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class LoginPage:
    """登录页面对象"""

    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_btn = page.locator("#login-btn")
        self.success_msg = page.locator("#success-msg")
        self.username_error = page.locator("#username-error")
        self.password_error = page.locator("#password-error")

    def goto(self):
        self.page.goto(f"file:///{BASE}/app/login.html")

    def login(self, user: str, pwd: str):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()

    def get_success_text(self) -> str:
        self.page.wait_for_selector("#success-msg.show", timeout=3000)
        return self.success_msg.inner_text()

    def get_username_error(self) -> str:
        self.page.wait_for_selector("#username-error.show", timeout=3000)
        return self.username_error.inner_text()

    def get_password_error(self) -> str:
        self.page.wait_for_selector("#password-error.show", timeout=3000)
        return self.password_error.inner_text()
