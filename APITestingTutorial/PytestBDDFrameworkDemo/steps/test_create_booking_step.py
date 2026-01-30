from pytest_bdd import *
from PytestBDDFrameworkDemo.common.common_steps import *
from PytestBDDFrameworkDemo.config.config import headers
from PytestBDDFrameworkDemo.payloads.payload import create_booking_payload
from PytestBDDFrameworkDemo.utils.constant import BOOKING_ID
from PytestBDDFrameworkDemo.utils.endpoints import BookingEndpoints
from PytestBDDFrameworkDemo.utils.response_validator import validate_key_in_response

scenarios("../features/create_booking.feature")

@given("User has booking details")
def create_payload(context):
    context.payload = create_booking_payload()

@when("User send booking details")
def send_booking_details(context,client):
    context.response = client.create_booking(BookingEndpoints.GET_ALL_BOOKINGS,context.payload,headers)

@then("response should contain bookingid")
def check_response(context,store_response):
    validate_key_in_response(context.response,BOOKING_ID)
    store_response.set_response(context.response)
    store_response.set(BOOKING_ID, context.response.json()[BOOKING_ID])
    print("create booking",context.response.json()[BOOKING_ID])
