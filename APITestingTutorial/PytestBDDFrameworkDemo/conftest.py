import pytest
from PytestBDDFrameworkDemo.clients.booking_client import BookingClient
from PytestBDDFrameworkDemo.config.config import headers
from PytestBDDFrameworkDemo.payloads.payload import auth_payload
from PytestBDDFrameworkDemo.utils.endpoints import BookingEndpoints
from PytestBDDFrameworkDemo.utils.response_validator import validate_status_code, validate_json_body, \
    validate_key_in_response
from PytestBDDFrameworkDemo.utils.status_codes import HTTPStatus
from PytestBDDFrameworkDemo.utils.store_response import StoreResponse


@pytest.fixture
def context():
    class Context:
        response = None
    return Context()        #create and return one object and these object is shared between all the steps of one scenario


@pytest.fixture
def client():
    return BookingClient()

@pytest.fixture(scope='session')
def auth_token(client,context):
    context.response = client.post_auth(BookingEndpoints.AUTH, auth_payload(), headers)
    validate_status_code(context.response.status_code,HTTPStatus.OK)
    validate_json_body(context.response.json())
    validate_key_in_response(context.response.json(),"token")
    token = context.response.json().get("token")
    return token

@pytest.fixture(scope="session")
def auth_headers(auth_token):
    return {
        "Content-Type": "application/json",
        "Cookie": f"token={auth_token}"
    }


'''Whenever any test will pass this fixture as a parameter then it will return an empty dictionary
This dictionary is: Created before each test and Destroyed after the test finishes
Think of it as a temporary notebook for one test'''
@pytest.fixture(scope="session")
def store_response():
    return StoreResponse()