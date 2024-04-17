import requests
from os import environ
import Weather.src.controllers as controllers

api_key = environ['API_KEY']
class Client:
    def __init__(self):
        self.api_key = api_key
    def get_data_from_api(self, city, state, country):
        r = requests.get(f"http://api.airvisual.com/v2/city?city={city}&state={state}&country={country}&key=" + self.api_key).json()
        print(r['data'])
        data = {"pollution": r['data']['current']['pollution'], "weather": r['data']['current']['weather']}
        controllers.Controller(controllers.AirRepository(), controllers.AirQuality()).add_air_quality(data)
        response = requests.post(url="http://localhost:5000/air", json=data)
        return response.text

    def get_data_from_client_by_timestamp(self, timestamp):
        return requests.get(url=f"http://localhost:5000/air/{timestamp}")






c=Client()
print(c.get_data_from_api("Los Angeles", "California", "USA"))
print(c.get_data_from_client_by_timestamp("2024-04-17T18:00:00.000Z").text)