

''' request.config.getoption("--browser_name")
request -> is a built-in argument that we pass while declaring fixtures
config -> represents pytest’s runtime configuration.
getoption -> Used to fetch a command-line option
--browser_name -> This is a custom option defined by you
Here browser name is given by us through command line argument which help in selecting the browser at runtime
'''

from Ecommerce.config.browser_factory import BrowserFactory
from Ecommerce.pages.LoginPage import LoginPage
from Ecommerce.utils.config_reader import get_config


import pytest
import allure

@pytest.fixture()
def setup():
    browser_name = get_config("env", "browser")
    #headless = get_config("env", "headless")
    headless = False
    #return driver based on the browser_name
    driver = BrowserFactory.get_driver(browser_name, headless)
    #get url from configuration file
    driver.get(get_config("app_url", "base_url"))
    driver.maximize_window()
    driver.implicitly_wait(get_config("timeouts", "implicit_wait"))
    yield driver
    driver.close()


## fixture chaining
@pytest.fixture
def login_Page(setup):
    return LoginPage(setup)

@pytest.fixture
def home_Page(login_Page):
    return login_Page.login(
        get_config("credentials","username"),
        get_config("credentials","password")
    )

@pytest.fixture
def checkout_page(home_Page):
    return home_Page.click_on_checkout_button()

@pytest.fixture
def address_page(checkout_page):
    return checkout_page.check_out()



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Take screenshot only if test failed during execution
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
