from selenium.webdriver.common.by import By
from Ecommerce.pages.AddressPage import AdressPage
from Ecommerce.utils.BasePage import BasePage

class CheckoutPage(BasePage):

    check_out_button =(By.CSS_SELECTOR, ".btn.btn-success")

    def check_out(self):
        self.click(self.check_out_button)
        return AdressPage(self.driver)