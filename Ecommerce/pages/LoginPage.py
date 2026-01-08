from selenium.webdriver.common.by import By

from Ecommerce.pages.HomePage import HomePage
from Ecommerce.utils.BasePage import BasePage


class LoginPage(BasePage):

    username = (By.ID, 'username')
    password = (By.ID, 'password')
    checkbox = (By.ID, 'terms')
    signUp_button = (By.ID, 'signInBtn')
    error_msg = (By.XPATH, "//div[contains(@class,'alert-danger')]")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.type(self.username, username)
        self.type(self.password, password)
        self.click(self.checkbox)
        self.click(self.signUp_button)


        return HomePage(self.driver)

    def is_error_message_visible(self):
        return self.is_visible(self.error_msg)
