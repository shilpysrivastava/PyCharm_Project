import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NewUser:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.first_name = (By.CSS_SELECTOR, "#firstname")
        self.last_name = (By.CSS_SELECTOR, "#lastname")
        self.username =(By.CSS_SELECTOR, "#userName")
        self.password = (By.CSS_SELECTOR, "#password")
        self.captcha = (By.CSS_SELECTOR, "#recaptcha-anchor")
        self.button = (By.XPATH, "//button[text()='Register']")
        #self.login_button =(By.ID, "gotologin")

    def register_user(self,first_name,last_name,username,password):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, "iframe[title='reCAPTCHA']"))
        self.wait.until(EC.presence_of_element_located(self.captcha))
        self.driver.find_element(*self.captcha).click()
        self.driver.switch_to.default_content()
        self.driver.find_element(*self.button).click()
        print("Clicked submit button")
        try:
            alert =self.wait.until(EC.alert_is_present())
            print("Alert text:", alert.text)
            alert.accept()
        except TimeoutException:
            print("No JS alert appeared")
        # assert alert_message.text == "Successfully registered"
        #self.driver.find_element(*self.login_button).click()


