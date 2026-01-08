'''Here we declare our all locators in the constructor and access those locator outside the
constructor using self keyword
*is basically used to unpack the tuple Here *self.username -> (By.ID, 'userName')
'''
import time

from selenium.webdriver.common.by import By
from pages.NewUserPage import NewUser
from pages.ProfilePage import Load_profile


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, 'userName')
        self.password = (By.ID, 'password')
        self.login_button = (By.ID, 'login')
        self.newUser_button = (By.ID, 'newUser')

    def open_registration_form(self):
        self.driver.find_element(*self.newUser_button).click()
        newUser = NewUser(self.driver)
        return newUser

    def login(self,username,password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        load_profile = Load_profile(self.driver)
        return load_profile

time.sleep(2)