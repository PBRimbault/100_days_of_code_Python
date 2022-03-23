#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import flight_data
import flight_search
import data_manager
import requests

sheety_endpoint = 'https://api.sheety.co/620f21c3e4a3c7a2cb9eeb1babe582cb/flightDeals/prices'
flight_tracker_api = 'WIQRubJHFEa7HJnm9BCw7K8Ecl85wPx3'

sheet_data = flight_data.FlightData(sheety_endpoint).checkData()
city_data = flight_search.FlightSearch(flight_tracker_api)

departure_iata_code = 'CPT'

# check_sheety_data = data_manager.DataManager(sheety_endpoint)
# check_sheety_data.checkData(sheet_data, city_data)

# received_flight_data = city_data.findFlightCost('PAR', 'NYC')
# print(received_flight_data['data'][0]['price'])
for item in sheet_data:
    destination_iata_code = item['iataCode']
    print(f'Checking cost from {departure_iata_code} to {destination_iata_code}')
    
    # destination_iata_code = 'IST'
    received_flight_data = city_data.findFlightCost(departure_iata_code, destination_iata_code)
    # print(received_flight_data)
    try:
        flight_cost = received_flight_data['data'][0]['price']
        print(f'Flight cost {flight_cost}')
    except IndexError:
        print(f'No flight info from {departure_iata_code} to {destination_iata_code}')
    else:
        if flight_cost < item['lowestPrice']:
            print(f'Found a cheap flight from {departure_iata_code} to {destination_iata_code}')
