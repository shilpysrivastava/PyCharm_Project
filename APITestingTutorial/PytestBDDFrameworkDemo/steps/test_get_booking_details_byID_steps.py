from pytest_bdd import scenarios, when
from PytestBDDFrameworkDemo.common.common_steps import *
from PytestBDDFrameworkDemo.utils.constant import BOOKING_ID
from PytestBDDFrameworkDemo.utils.endpoints import BookingEndpoints

scenarios("../features/get_booking_details_byID.feature")

'''Here we write the step implementation of the feature file'''

@when("I fetch booking details for created booking")
def fetch_booking_details(context,client,store_response):
    id= store_response.get(BOOKING_ID)
    context.response = client.getBookings(BookingEndpoints.GET_BOOKING_BY_ID.format(id=id))


@then("print all the booking details for created booking")
def print_details(context):
    response = context.response.json()
    print(f" get bookingdetails {response}")