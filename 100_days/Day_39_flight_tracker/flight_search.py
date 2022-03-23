import requests
import datetime as dt

class FlightSearch:
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.query_url = 'https://tequila-api.kiwi.com/locations/query'
        self.search_url = 'https://tequila-api.kiwi.com/search'

    def checkCity(self, city):
        self.city = city
        self.flight_parameters = {
            "term": self.city,
            "location_types": 'city',
            "limit": '1',
        }
        self.headers = {
            "apikey": self.api_key
        }
    
        self.flight_info = requests.get(url=self.query_url, params=self.flight_parameters, headers=self.headers).json()
        return self.flight_info['locations'][0]['code']

    def findFlightCost(self, destinationCode, departureCode):
        self.destinationCode = destinationCode
        self.departureCode = departureCode
        self.today_date = dt.date.today()
        self.return_date = self.today_date + dt.timedelta(days=180)

        self.today_date = self.today_date.strftime("%d/%m/%Y")
        self.return_date = self.return_date.strftime("%d/%m/%Y")

        self.search_parameters = {
            "fly_from": self.departureCode,
            "fly_to": self.destinationCode,
            "date_from": self.today_date,
            "date_to" : self.return_date,
            "adults" : 1,
            "one_for_city" : 1,
            "limit" : 1,
            "curr" : 'ZAR',
        }
        self.headers = {
            "apikey": self.api_key
        }
    
        self.available_flights = requests.get(url=self.search_url, params=self.search_parameters, headers=self.headers).json()
        return self.available_flights