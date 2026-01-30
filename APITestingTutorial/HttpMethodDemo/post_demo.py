import requests

def post_addbook():
    addbook_response = requests.post("http://216.10.245.166/Library/Addbook.php",
                  json={
    "name":"python",
    "isbn":"TMFDS",
    "aisle":"417",
    "author":"John Sweet"
    },headers={"Content-Type":"application/json"},)

    addbook_response_json = addbook_response.json()
    print(addbook_response_json)


def post_addProduct():
    addproduct_response = requests.post("https://automationexercise.com/api/productsList")
    assert addproduct_response.status_code == 200
    addproduct_response_json = addproduct_response.json()
    print(addproduct_response_json)
    assert addproduct_response_json["responseCode"] == 405


def post_login():
    login_response = requests.post("https://restful-booker.herokuapp.com/auth",
                                   json={"username" : "admin",
                                        "password" : "password123"},
                                   headers={"Content-Type":"application/json"},)
    assert login_response.status_code == 200
    print(login_response.json())



def createbooking():

    createbookingresponse = requests.post("https://restful-booker.herokuapp.com/booking",
                  json={
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
},headers={"Content-Type":"application/json"},)
    print(createbookingresponse.status_code)
    print(createbookingresponse.json())


#createbooking()
post_login()
