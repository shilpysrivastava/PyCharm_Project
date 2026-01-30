from selenium.webdriver.common.by import By
from Ecommerce.utils.BasePage import BasePage


class AdressPage(BasePage):

    send_country = (By.CSS_SELECTOR, "#country")
    country_list = (By.CSS_SELECTOR, "div[class='suggestions'] ul")
    term_condition_checkbox = (By.CSS_SELECTOR, "label[for='checkbox2']")
    purchase_button = (By.CSS_SELECTOR, "input[value='Purchase']")
    alert_message = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")



    def enterCountry(self):
        self.type(self.send_country,"in",False)

    def get_All_CountryList(self):
        return self.driver.find_elements(*self.country_list)

    def addAdress(self,country_list):
        for country in country_list:
            if country.text == "India":
                country.click()
                break

    def click_term_condition_checkbox(self):
        self.click(self.term_condition_checkbox)

    def click_purchase_button(self):
        self.click(self.purchase_button)

    def get_success_message(self):
        return self.get_text(self.alert_message)