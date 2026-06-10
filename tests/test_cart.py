import allure


@allure.feature("购物车模块")
class TestCart:

    @allure.story("空购物车")
    def test_empty_cart(self, cart_page):
        assert cart_page.is_empty()

    @allure.story("添加后购物车有商品")
    def test_cart_after_add(self, product_page):
        # 同一个 page 上操作：加商品 → 跳到购物车页面
        product_page.add_to_cart("无线蓝牙耳机")
        product_page.add_to_cart("机械键盘")

        # 跳到购物车（同一个浏览器上下文，localStorage 才能共享）
        product_page.page.goto(
            product_page.page.url.replace("index.html", "cart.html")
        )
        # 用同一个 page 创建 CartPage 来检查
        from pages.cart_page import CartPage
        cp = CartPage(product_page.page)
        assert cp.get_item_count() == 2

    @allure.story("删除商品")
    def test_remove_item(self, product_page):
        product_page.add_to_cart("保温咖啡杯")
        product_page.page.goto(
            product_page.page.url.replace("index.html", "cart.html")
        )
        from pages.cart_page import CartPage
        cp = CartPage(product_page.page)
        assert cp.get_item_count() == 1
        cp.remove_item("保温咖啡杯")
        assert cp.is_empty()

    @allure.story("修改数量")
    def test_change_qty(self, product_page):
        product_page.add_to_cart("运动智能手环")
        product_page.page.goto(
            product_page.page.url.replace("index.html", "cart.html")
        )
        from pages.cart_page import CartPage
        cp = CartPage(product_page.page)
        assert cp.get_qty("运动智能手环") == 1
        cp.change_qty("运动智能手环", 1)
        assert cp.get_qty("运动智能手环") == 2

    @allure.story("总价计算")
    def test_total_price(self, product_page):
        product_page.add_to_cart("无线蓝牙耳机")
        product_page.add_to_cart("保温咖啡杯")
        product_page.page.goto(
            product_page.page.url.replace("index.html", "cart.html")
        )
        from pages.cart_page import CartPage
        cp = CartPage(product_page.page)
        assert "$388" in cp.get_total_price()
