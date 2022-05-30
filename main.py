import os
import requests
from datetime import datetime
EXERCISE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETS_URL = os.getenv("SHEETS_URL")
today = datetime.now()
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
workout_input = input("What workouts did you do today?\n")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

workout_params = {
    "query": workout_input,
    "gender": "male",
    "age": os.environ.get("AGE")
}
workout_response = requests.post(url=EXERCISE_URL,json=workout_params,headers=headers)
workout_data = workout_response.json()
print(workout_data)
my_range = len(workout_data["exercises"])
for i in range(my_range):
    print(i)
    sheet_params = {
        "workout":{
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": (workout_data["exercises"][i]["name"]).title(),
            "duration": workout_data["exercises"][i]["duration_min"],
            "calories": workout_data["exercises"][i]["nf_calories"]

        }
    }
    sheets_response = requests.post(url=SHEETS_URL, json=sheet_params)
    print(sheets_response.text)

#Each time we answer the question, we want a new row with date, time, exercise, duration, and calories


