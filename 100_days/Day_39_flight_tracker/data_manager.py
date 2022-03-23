import flight_data
import flight_search
import requests

class DataManager:
    
    def __init__(self, sheety_endpoint):
        self.sheety_endpoint = sheety_endpoint        

    def checkData(self, sheet_data, city_data):    
        self.sheet_data = sheet_data
        self.city_data = city_data
    
        for city in self.sheet_data:
            if city['iataCode'] == '':        
                NewIataCode = (self.city_data.checkCity(city['city']))
                city_input = {
                    "price" : {
                        "iataCode" : NewIataCode,
                    }
                }
                sheety_put_endpoint = self.sheety_endpoint + '/' + str(city['id'])
                city_data_payload = requests.put(url=sheety_put_endpoint, json=city_input)