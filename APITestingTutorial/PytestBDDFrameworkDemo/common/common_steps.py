from pytest_bdd import given, then
from PytestBDDFrameworkDemo.utils.response_validator import *
from PytestBDDFrameworkDemo.utils.status_codes import HTTPStatus

''''there are multiple steps in feature file which are common for the different scenario so we will write all the common
steps in this file. based on the given,when,then statement bdd will execute these file but we need to import this file in
our test file to get all function imported
'''

@given("booking service is available")
def booking_service_is_available():
    pass

@then("response status code should be 200")
def validate_responsecode(context):
    validate_status_code(context.response, HTTPStatus.OK)

@then("response should be json")
def validate_response(context):
    validate_json_body(context.response)

