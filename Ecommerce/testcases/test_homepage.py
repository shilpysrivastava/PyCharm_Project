

from pytest_check import check


def test_add_product_to_cart(home_Page):
    productList=home_Page.get_all_products()
    check.equal(len(productList), 4, f"Expected list length 4, found {len(productList)}")
    home_Page.add_to_cart(productList)


def test_click_on_cart_button(home_Page):
        productList = home_Page.get_all_products()
        if (len(productList) > 0):
            home_Page.click_on_checkout_button()
            print("Clicked 'Check out Checkout button'")
        else:
            print("Not Clicked 'Check out button not clicked button'")











