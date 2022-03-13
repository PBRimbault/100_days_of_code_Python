import requests
from datetime import datetime as dt

USERNAME = 'patrickrimbault'
TOKEN = '>Up36cpktm;kX]/@'
GRAPH_ID = 'graph1'

GRAPH_HARD_LINK = 'https://pixe.la/v1/users/patrickrimbault/graphs/graph1.html'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token' : TOKEN,
    'username' : USERNAME,
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id' : 'graph1',
    'name' : 'Cycling Graph',
    'unit' : 'Km',
    'type' : 'float',
    'color' : 'ajisai',
}

headers = {
    'X-USER-TOKEN' : TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

date = dt(year=2022, month=3, day=10)

graph_update = {
    'date' : date.strftime("%Y%m%d"),
    'quantity' : '14.2',
}

# response = requests.post(url=pixel_creation_endpoint, json=graph_update, headers=headers)
# print(response.text)

PIXEL_DATE = '20220311'

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{PIXEL_DATE}"

pixel_update = {
    'quantity' : '42.0',
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update, headers=headers)
# print(response.text)

PIXEL_DELETE_DATE = '20220311'

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{PIXEL_DELETE_DATE}"

response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)