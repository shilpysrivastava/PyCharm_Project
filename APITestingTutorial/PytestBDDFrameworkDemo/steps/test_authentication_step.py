from pytest_bdd import when, scenarios, given,then
from PytestBDDFrameworkDemo.config.config import headers
from PytestBDDFrameworkDemo.payloads.payload import  invalid_auth_payload
from PytestBDDFrameworkDemo.utils.endpoints import BookingEndpoints
from PytestBDDFrameworkDemo.common.common_steps import then
from PytestBDDFrameworkDemo.utils.response_validator import *

scenarios("../features/auth.feature")

@given("Valid username and password")
def valid_auth(context):
    context.payload= invalid_auth_payload()


@when("User send request with valid username and password")
def request_token(context,client):
    context.response = client.post_auth(BookingEndpoints.AUTH,context.payload,headers)

@then("auth token generate successfully")
def auth_token_generate(context):
    validate_key_in_response(context.response,"token")
    print("token",context.response.json())


