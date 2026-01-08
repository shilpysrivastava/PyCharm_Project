import pytest_check as check

from utils.config_reader import get_config



def test_valid_login(login_Page):
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


