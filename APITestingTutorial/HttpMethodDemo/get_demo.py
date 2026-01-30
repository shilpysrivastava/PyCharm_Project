import requests

def get_book():
    getbookresponse= requests.get("http://216.10.245.166/Library/GetBook.php",params={'AuthorName':'John Sweet'})
    print(getbookresponse.status_code)
    print(getbookresponse.json())

def get_bookId():
    getIdresponse = requests.get("https://restful-booker.herokuapp.com/booking")
    #getIdresponse = requests.get("https://restful-booker.herokuapp.com/booking",params={'firstname':'sally', 'lastname':'brown'})
    print(getIdresponse.status_code)
    print(getIdresponse.json())
    print(len(getIdresponse.json()))


def getbookingdetails():
    id = 1
    url = f"https://restful-booker.herokuapp.com/booking/{id}"
    getbookingresponse= requests.get(url)
    print(getbookingresponse.status_code)
    print(getbookingresponse.json())


get_bookId()
#getbookingdetails()