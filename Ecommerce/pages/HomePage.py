import time

from selenium.webdriver.common.by import By

from pages.CheckOutPage import CheckoutPage
from utils.BasePage import BasePage


class HomePage(BasePage):

    product_list =(By.CSS_SELECTOR, "app-card[class='col-lg-3 col-md-6 mb-3']")
    add_to_cart_button = (By.CSS_SELECTOR, "div div button[class='btn btn-info']")
    checkout_button = (By.CSS_SELECTOR,".nav-link.btn.btn-primary")

    def get_all_products(self):
        return self.wait_for_all_elements(self.product_list)

    def add_to_cart(self, productList):
        for product in productList:
            product.find_element(*self.add_to_cart_button).click()

    def click_on_checkout_button(self):
        self.click(self.checkout_button)
        return CheckoutPage(self.driver)







