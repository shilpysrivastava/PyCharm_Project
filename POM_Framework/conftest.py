''' request.config.getoption("--browser_name")
request -> is a built-in argument that we pass while declaring fixtures
config -> represents pytest’s runtime configuration.
getoption -> Used to fetch a command-line option
--browser_name -> This is a custom option defined by you
Here browser name is given by us through command line argument which help in selecting the browser at runtime
'''

import pytest
from selenium import webdriver

#This is the way to register option through command line argument
#pytest_addoption is a pytest hook , Automatically called by pytest at startup
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Browser name: chrome or firefox"
    )

@pytest.fixture()
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.get("https://demoqa.com/login")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()
