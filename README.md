# 电商自动化测试项目

基于 Playwright + pytest 的电商网站端到端自动化测试框架。

## 项目结构
```
├── app/              # 被测网站（4 个本地页面）
├── pages/            # POM 页面对象
├── tests/            # 测试用例
└── pytest.ini        # pytest 配置
```

## 被测功能
| 页面 | 功能 |
|------|------|
| 登录 | 表单验证、错误提示、登录成功 |
| 商品列表 | 商品展示、搜索过滤、加入购物车 |
| 购物车 | 增删改查、数量调整、总价计算 |
| 结算 | 表单验证、手机号校验、订单提交 |

## 技术栈
Python 3.13 | Playwright | pytest | Allure

## 运行测试
```bash
pip install pytest playwright allure-pytest
playwright install chromium
pytest tests/ -v
```

## 测试结果
18 条用例 · 4 个模块 · 全部通过 ✅
