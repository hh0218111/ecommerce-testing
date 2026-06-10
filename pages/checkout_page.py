import os
from playwright.sync_api import Page

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class CheckoutPage:
    """结算页面对象"""

    def __init__(self, page: Page):
        self.page = page
        self.receiver = page.locator("#receiver")
        self.phone = page.locator("#phone")
        self.address = page.locator("#address")
        self.province = page.locator("#province")
        self.payment = page.locator("#payment")
        self.submit_btn = page.locator("#submit-btn")
        self.success_modal = page.locator("#success-modal")
        self.checkout_total = page.locator("#checkout-total")
        # error messages
        self.receiver_error = page.locator("#receiver-error")
        self.phone_error = page.locator("#phone-error")
        self.address_error = page.locator("#address-error")

    def goto(self):
        self.page.goto(f"file:///{BASE}/app/checkout.html")

    def fill_form(self, receiver: str, phone: str, address: str, province: str, payment: str):
        self.receiver.fill(receiver)
        self.phone.fill(phone)
        self.address.fill(address)
        self.province.select_option(province)
        self.payment.select_option(payment)

    def submit(self):
        self.submit_btn.click()

    def get_total(self) -> str:
        return self.checkout_total.inner_text()

    def is_success_modal_visible(self) -> bool:
        self.page.wait_for_timeout(1200)
        return "show" in (self.success_modal.get_attribute("class") or "")

    def has_error(self, field: str) -> bool:
        err = self.page.locator(f"#{field}-error")
        return "show" in (err.get_attribute("class") or "")
