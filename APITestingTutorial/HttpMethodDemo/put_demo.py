import requests


def updatedata():
    id = 1
    url = f"https://restful-booker.herokuapp.com/booking/{id}"
    updatedataresponse = requests.put(url,
                 headers={"Content-Type":"application/json","Accept":"application/json", "Cookie": "token=064ecb167c84df3"},
                 json= {
    "firstname" : "James",
    "lastname" : "Brown",
    "totalprice" : 112,
    "depositpaid" : False,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Dinner"
})
    print(updatedataresponse.status_code)
    print(updatedataresponse.text)
    print(updatedataresponse.headers)



updatedata()