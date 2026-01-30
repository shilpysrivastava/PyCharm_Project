from pytest_bdd import scenarios, when
from PytestBDDFrameworkDemo.common.common_steps import *
from PytestBDDFrameworkDemo.payloads.payload import update_booking_payload
from PytestBDDFrameworkDemo.utils.constant import BOOKING_ID
from PytestBDDFrameworkDemo.utils.endpoints import BookingEndpoints


scenarios("../features/partial_update_booking.feature")

@when("Send bookingid with updated value")
def send_bookingid(context,client,store_response,auth_headers):
    id = store_response.get(BOOKING_ID)
    headers = auth_headers.copy()
    headers["Accept"] = "application/json"
    context.response = client.update_booking(BookingEndpoints.GET_BOOKING_BY_ID.format(id=id),update_booking_payload(),headers)

@then("response should print updated value")
def validate_response(context):
    print("update booking",context.response.json())