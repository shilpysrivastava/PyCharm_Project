import json

import allure
import pytest
import pytest_check as check

from Ecommerce.utils.config_reader import get_config

file_path = r"E:\PyCharm_Project\Ecommerce\testdata\login_data.json"
def login_data():
    with open(file_path, "r") as f:
        data = json.load(f)      #reading data from json file
        print(data)
        print(type(data))
        return data

@allure.title("Verify user can login with the valid credentials")
@allure.feature("Login")
@allure.severity(allure.severity_level.BLOCKER)
@allure.testcase("testcase t01")
@allure.story("Valid Login")
@allure.description("This test verifies that user is able to login using valid username and password")
def test_valid_login(login_Page):
    with allure.step("Enter username and password"):
        login_Page.login(
            get_config("credentials","username"),
            get_config("credentials","password")
        )
        check.is_false(
            login_Page.is_error_message_visible(),
            "Error message is visible on login success"
        )


def test_invalid_login(login_Page):
    login_Page.login("ajay","ajay")
    check.is_true(login_Page.is_error_message_visible(),
    "Error message is not visible on login failure")


@allure.story("Data driven report")
@pytest.mark.parametrize("test_data", login_data())               #passing here the JSON file
def test_valid_and_invalid_login(login_Page,test_data):
    allure.dynamic.title(f"Login with user={test_data["username"]} expect={test_data["expected"]}")
    login_Page.login(test_data["username"],test_data["password"])
    if test_data["expected"] == "success":
        print("Test case is valid")
        check.is_true(login_Page.is_error_message_visible(),                 #intenionally failling the test case
                      "Error message is not visible on login failure")
    else:
        print("Test case is invalid")
        check.is_true(login_Page.is_error_message_visible(),
                      "Error message is not visible on login failure")


