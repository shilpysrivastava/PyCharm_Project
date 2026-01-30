from PytestBDDFrameworkDemo.config.config import username, password


def auth_payload():
    return {
        "username": username,
        "password": password
    }

def invalid_auth_payload():
    return {
        "username": "username",
        "password": "password"
    }

def create_booking_payload():
    return {
    "firstname" : "Rahul",
    "lastname" : "Sheety",
    "totalprice" : 5000,
    "depositpaid" : False,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

def update_booking_payload():
    return {
        "firstname": "Raj",
        "lastname": "Sharma",
        "totalprice": 4000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2026-01-01"
        },
        "additionalneeds": "dinner"
    }

def update_partial_booking_payload():
    return {
    "firstname" : "Tyler",
    "lastname" : "Sweet"
}

