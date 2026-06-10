import allure


@allure.feature("结算模块")
class TestCheckout:

    @allure.story("空表单提交显示错误")
    def test_empty_form_errors(self, checkout_page):
        checkout_page.submit()
        assert checkout_page.has_error("receiver")
        assert checkout_page.has_error("phone")
        assert checkout_page.has_error("address")

    @allure.story("手机号格式错误")
    def test_invalid_phone(self, checkout_page):
        checkout_page.fill_form("张三", "12345", "深圳", "广东", "wechat")
        checkout_page.submit()
        assert checkout_page.has_error("phone")

    @allure.story("完整填写提交成功")
    def test_successful_checkout(self, product_page):
        # 先加购物车
        product_page.add_to_cart("无线蓝牙耳机")
        product_page.add_to_cart("机械键盘")

        # 跳到结算页（同一个 page，localStorage 才能共享）
        product_page.page.goto(
            product_page.page.url.replace("index.html", "checkout.html")
        )

        from pages.checkout_page import CheckoutPage
        chp = CheckoutPage(product_page.page)
        chp.fill_form("张三", "13800138000", "广东省深圳市", "广东", "wechat")
        chp.submit()
        assert chp.is_success_modal_visible()
