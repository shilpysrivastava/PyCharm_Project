import requests

from PytestBDDFrameworkDemo.config.config import base_url

'''In this file we will declare all the get/post/put/delete request. Basically from here we hit the url using request library'''

class BookingClient:


    def get_BookingIds(self,endpoint):
        return requests.get(f"{base_url}{endpoint}")

    def getBookings(self,endpoint):
        print(f"{base_url}{endpoint}")
        return requests.get(f"{base_url}{endpoint}")

    def post_auth(self,endpoint,payload,headers):
        return requests.post(f"{base_url}{endpoint}", json=payload, headers=headers)


    def create_booking(self,endpoint,payload,headers):
        return requests.post(f"{base_url}{endpoint}", json=payload, headers=headers)

    def update_booking(self,endpoint,payload,headers):
        return requests.put(f"{base_url}{endpoint}",json=payload, headers=headers)

    def partial_update_booking(self,endpoint,payload,headers):
        return requests.patch(f"{base_url}{endpoint}",json=payload, headers=headers)

    def delete_booking(self,endpoint,headers):
        return requests.delete(f"{base_url}{endpoint}", headers=headers)



