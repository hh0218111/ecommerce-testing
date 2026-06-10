import allure


@allure.feature("登录模块")
class TestLogin:

    @allure.story("正常登录")
    def test_login_success(self, login_page):
        login_page.login("admin", "123456")
        text = login_page.get_success_text()
        assert "成功" in text

    @allure.story("用户名为空")
    def test_login_empty_username(self, login_page):
        login_page.login("", "123456")
        error = login_page.get_username_error()
        assert "不能为空" in error

    @allure.story("密码太短")
    def test_login_short_password(self, login_page):
        login_page.login("admin", "123")
        error = login_page.get_password_error()
        assert "至少6位" in error

    @allure.story("用户名和密码都为空")
    def test_login_both_empty(self, login_page):
        login_page.login("", "")
        assert "不能为空" in login_page.get_username_error()
        assert "至少6位" in login_page.get_password_error()
