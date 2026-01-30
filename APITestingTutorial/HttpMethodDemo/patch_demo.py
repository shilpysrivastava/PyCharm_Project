import requests


def partialupdatebooking():
    id = 1
    url = f"https://restful-booker.herokuapp.com/booking/{id}"
    partialupdatebookingresponse = requests.patch(url,
                                                  headers={"Content-Type": "application/json","Accept": "application/json", "Cookie": "token=064ecb167c84df3"},
                                                  json={
                                                      "firstname": "James",
                                                      "lastname": "Brown"
                                                 })
    print(partialupdatebookingresponse.status_code)
    print(partialupdatebookingresponse.json())

partialupdatebooking()

