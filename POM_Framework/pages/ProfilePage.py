import time

from selenium.webdriver.common.by import By

from utils.BasePage import BasePage


class Load_profile(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.gotoStoreButton = (By.CSS_SELECTOR,'#gotoStore')

    def userProfile(self):
        self.click(self.gotoStoreButton)



time.sleep(2)

