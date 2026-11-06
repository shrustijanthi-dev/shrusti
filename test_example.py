from playwright.sync_api import Page, expect


def test_products(setup_zemicon: Page):
    products = setup_zemicon.get_by_role("button", name="Products").first
    expect(products).to_be_visible()


class TestZemicon:
    def test_1(self, setup_zemicon: Page):
        expect(setup_zemicon).to_have_url("https://zemicon.in/")

    def test_2(self, setup_zemicon: Page):
        categories = setup_zemicon.get_by_role("button", name="Categories").first
        expect(categories).to_be_visible()
