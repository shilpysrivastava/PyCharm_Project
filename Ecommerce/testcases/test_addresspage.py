import pytest_check as check


def test_enter_country(address_page):
    # checkout_page = home_Page.click_on_checkout_button()
    # address_page = checkout_page.check_out()

    address_page.enterCountry()
    country_list= address_page.get_All_CountryList()
    assert len(country_list) >0, f"Expected at least 4 products, found {len(country_list)}"
    address_page.addAdress(country_list)


def test_click_term_condition(address_page):
    address_page.click_term_condition_checkbox()


def test_click_purchase(address_page):
    address_page.click_purchase_button()
    success_message = address_page.get_success_message()
    # Soft assert that "Success" is in message
    check.is_in("NotSuccess", success_message, f"Expected success, found '{success_message}'")






