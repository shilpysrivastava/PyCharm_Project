from pytest_bdd import scenarios, when
from PytestBDDFrameworkDemo.common.common_steps import *
from PytestBDDFrameworkDemo.utils.endpoints import BookingEndpoints

scenarios("../features/get_bookingIds.feature")

@when("I send a get request")
def fetch_all_booking_ids(context,client):
    context.response = client.get_BookingIds(BookingEndpoints.GET_ALL_BOOKINGS)

@then("response should not be empty")
def validate_list_is_not_empty(context):
    validate_list_not_empty(context.response)

@then("response should contain booking ids")
def validate_key(context):
    response_json = context.response.json()
    for item in response_json:
        assert "bookingid" in item
        print(f"bookingid: {item['bookingid']}")






