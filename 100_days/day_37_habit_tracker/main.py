import requests

pixela_endpoint = 'https://pixe.la/v1/user'

user_params = {
    'token' : '',
    'username' : 'patrickrimbault',
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes',
}

requests.post(pixela_endpoint)