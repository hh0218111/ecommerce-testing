import pytest, allure


@allure.feature("商品模块")
class TestProduct:

    @allure.story("商品列表加载")
    def test_products_loaded(self, product_page):
        count = product_page.get_product_count()
        assert count == 8, f"应有8个商品，实际{count}个"

    @allure.story("搜索商品")
    @pytest.mark.parametrize("keyword,expected_count", [
        ("耳机", 1),
        ("数码", 4),
        ("zzzz", 0),
    ])
    def test_search(self, product_page, keyword, expected_count):
        product_page.search(keyword)
        count = product_page.get_product_count()
        assert count == expected_count

    @allure.story("加入购物车")
    def test_add_to_cart(self, product_page):
        assert product_page.get_cart_count() == 0
        product_page.add_to_cart("无线蓝牙耳机")
        assert product_page.get_cart_count() == 1
        assert product_page.is_toast_shown()

    @allure.story("多次加入购物车")
    def test_add_multiple(self, product_page):
        product_page.add_to_cart("无线蓝牙耳机")
        product_page.add_to_cart("机械键盘")
        product_page.add_to_cart("无线蓝牙耳机")
        assert product_page.get_cart_count() == 3
