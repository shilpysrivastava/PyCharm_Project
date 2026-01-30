''''This class will store all the json response and we can use it to set and get the data'''
"""
   Holds test-scoped data like responses and extracted values.
   One instance per test.
   """

class StoreResponse:

    def __init__(self):
        self.response = None 
        self.data ={}           #Dictionary to store custom key-value data

    def set_response(self, response):
        self.response = response       #Saves the API response into the context

    def get_response(self):
        if self.response is None:
            raise ValueError("Response is not set in test context")
        return self.response

    def set(self,key,value):        #Store any extracted value
        self.data[key] = value

    def get(self,key):
        if key not in self.data:
            raise KeyError(f"Key '{key}' not found in test context")
        return self.data[key]