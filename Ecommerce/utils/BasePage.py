from selenium.common import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Ecommerce.utils.config_reader import get_config


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,get_config("timeouts","explicit_wait"))


    # =========================
    # WAIT METHODS
    # =========================

    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_invisibility(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_all_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    # =========================
    # ACTION METHODS
    # =========================

    def click(self, locator):
        self.wait_for_clickable(locator).click()

    def type(self, locator, text, clear=True):
        element = self.wait_for_visibility(locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait_for_visibility(locator).text

    def is_visible(self, locator):
        try:
            return self.wait_for_visibility(locator).is_displayed()
        except (
                TimeoutException):
            return False

    # =========================
    # DROPDOWN METHODS
    # =========================

    def select_by_text(self, locator, text):
        Select(self.wait_for_visibility(locator)).select_by_visible_text(text)

    def select_by_value(self, locator, value):
        Select(self.wait_for_visibility(locator)).select_by_value(value)

    def select_by_index(self, locator, index):
        Select(self.wait_for_visibility(locator)).select_by_index(index)

    # =========================
    # BROWSER UTILS
    # =========================

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def refresh(self):
        self.driver.refresh()

    def back(self):
        self.driver.back()

    # =========================
    # ASSERTION HELPERS
    # =========================

    def wait_for_url_contains(self, text):
        return self.wait.until(EC.url_contains(text))

    def wait_for_title_is(self, title):
        return self.wait.until(EC.title_is(title))
