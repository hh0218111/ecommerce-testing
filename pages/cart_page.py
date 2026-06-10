import os
from playwright.sync_api import Page

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class CartPage:
    """购物车页面对象"""

    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator("#cart-items")
        self.empty_msg = page.locator("#empty-msg")
        self.total_price = page.locator("#total-price")
        self.checkout_btn = page.locator("#checkout-btn")

    def goto(self):
        self.page.goto(f"file:///{BASE}/app/cart.html")

    def get_item_count(self) -> int:
        return self.cart_items.locator(".cart-item").count()

    def get_item_names(self) -> list:
        return self.cart_items.locator(".name").all_inner_texts()

    def get_total_price(self) -> str:
        return self.total_price.inner_text()

    def is_empty(self) -> bool:
        return self.empty_msg.is_visible()

    def remove_item(self, item_name: str):
        item = self.cart_items.locator(".cart-item", has_text=item_name)
        item.locator(".remove").click()
        self.page.wait_for_timeout(300)

    def change_qty(self, item_name: str, delta: int):
        item = self.cart_items.locator(".cart-item", has_text=item_name)
        if delta > 0:
            item.locator("[aria-label='增加']").click()
        else:
            item.locator("[aria-label='减少']").click()
        self.page.wait_for_timeout(300)

    def get_qty(self, item_name: str) -> int:
        item = self.cart_items.locator(".cart-item", has_text=item_name)
        qty_span = item.locator("[id^='qty-']")
        return int(qty_span.inner_text())

    def go_checkout(self):
        self.checkout_btn.click()
