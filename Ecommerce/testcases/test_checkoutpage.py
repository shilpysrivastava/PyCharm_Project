from pytest_check import check

def test_validate_chekout(checkout_page):
    checkout_page.check_out()


