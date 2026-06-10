import os
from playwright.sync_api import Page

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ProductPage:
    """商品列表页面对象"""

    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator("#search-input")
        self.product_list = page.locator("#product-list")
        self.cart_count = page.locator("#cart-count")
        self.toast = page.locator("#toast")
        self.cart_link = page.locator("#cart-link")

    def goto(self):
        self.page.goto(f"file:///{BASE}/app/index.html")

    def search(self, keyword: str):
        self.search_input.fill(keyword)
        self.page.wait_for_timeout(300)

    def get_product_count(self) -> int:
        return self.product_list.locator(".card").count()

    def get_product_names(self) -> list:
        return self.product_list.locator(".card-body h3").all_inner_texts()

    def add_to_cart(self, product_name: str):
        card = self.product_list.locator(".card", has_text=product_name)
        card.locator("button").click()
        self.page.wait_for_timeout(500)

    def get_cart_count(self) -> int:
        text = self.cart_count.inner_text()
        return int(text) if text else 0

    def is_toast_shown(self) -> bool:
        return "show" in (self.toast.get_attribute("class") or "")
