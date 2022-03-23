import requests

class FlightData:
    def __init__(self, sheety_url):
        self.sheety_url = sheety_url
        
    def checkData(self):
        self.prices = requests.get(url=self.sheety_url).json()
        return self.prices['prices']