import requests



def deletebooking():
    id = 2
    url = f"https://restful-booker.herokuapp.com/booking/{id}"
    deletebookingresponse = requests.delete(url,headers={"Content-Type": "application/json", "Cookie": "token=21c41808c95cb18"})
    print(deletebookingresponse.status_code)
    print(deletebookingresponse.text)


deletebooking()