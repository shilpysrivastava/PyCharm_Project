from pytest_bdd import scenarios, when
from PytestBDDFrameworkDemo.common.common_steps import *
from PytestBDDFrameworkDemo.utils.constant import BOOKING_ID
from PytestBDDFrameworkDemo.utils.endpoints import BookingEndpoints


scenarios("../features/delete_booking.feature")

@when("send bookingid")
def send_bookingid(context,client,store_response,auth_headers):
    id = store_response.get(BOOKING_ID)
    context.response = client.delete_booking(BookingEndpoints.GET_BOOKING_BY_ID.format(id=id),auth_headers)

@then("response code should be 201")
def validate_statuscode(context):
    validate_status_code(context.response, HTTPStatus.CREATED)

@then("response contain text created")
def validate_response(context):
    assert "created" in context.response.text
    print("Delete booking",context.response.json())