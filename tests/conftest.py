import pytest, os, allure
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def login_page(page: Page):
    lp = LoginPage(page)
    lp.goto()
    return lp


@pytest.fixture
def product_page(page: Page):
    pp = ProductPage(page)
    pp.goto()
    return pp


@pytest.fixture
def cart_page(page: Page):
    cp = CartPage(page)
    cp.goto()
    return cp


@pytest.fixture
def checkout_page(page: Page):
    chp = CheckoutPage(page)
    chp.goto()
    return chp


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(path=f"screenshots/{item.name}.png")
