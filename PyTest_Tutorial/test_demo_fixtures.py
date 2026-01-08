'''fixtures are used for setup and teardown
Anything before yield → setup
Anything after yield → teardown

autouse=True-> Fixture runs without explicitly mentioning it in the test.
'''
import pytest


@pytest.fixture()
def sample_profile():
    print("This is sample_profile test case,I will launch first as I m setup fixture")
    yield
    print("This is teardown test case")


def test_profileUpdate():
    print("This is test profile update test case, I will launch after fixture")