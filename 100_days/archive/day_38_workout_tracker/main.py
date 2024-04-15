import requests
from datetime import datetime as dt

APP_ID = '37f92d85'
API_KEY = '4353ec5e602b68dd5abd403b0d0a6132'

SHEETY_USERNAME = 'patrickrimbault'
SHEETY_PASSWORD = 'g4T<Hud6e"5^{ypR'

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = 'https://api.sheety.co/620f21c3e4a3c7a2cb9eeb1babe582cb/workoutTracking/workouts'

headers = {
    'x-app-id' : APP_ID,
    'x-app-key' : API_KEY
}

exercise_params = {
    'query' : input('What exercise did you do? '),
    'gender' : 'male',
    'weight_kg':72.5,
    'height_cm':179.64,
    'age':30
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers).json()

print(response)

for activity in response['exercises']:
    print(activity)
    exercise_date = dt.now().strftime("%d/%m/%Y")
    exercise_time = dt.now().strftime("%H:%M:%S")
    exercise_type = activity['name']
    exercise_duration = activity['duration_min']
    exercise_nf_calories = activity['nf_calories']

    exercise_input = {
        "workout" : {
            "date" : exercise_date,
            "time" : exercise_time,
            "exercise" : exercise_type.title(),
            "duration" : exercise_duration,
            "calories" : exercise_nf_calories,
        }
    }

    excercise_payload = requests.post(url=sheety_endpoint, json=exercise_input)