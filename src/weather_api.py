import requests
from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
if api_key is None:
    raise RuntimeError("API_KEY not set. Please create a .env file.")

@dataclass
class ClimateInfo:
    date: str
    hour: str
    country: str
    city_name: str
    region: str
    condition: str
    chance_of_rain: int
    feels_like: float
    humidity: float
    temperature: float
    winds: float

class Api_management:

    def __init__(self, city):
        self.parameters = {
            "key": api_key,
            "q": city
        }

    def extract_climate_info(self) -> requests.Response:
        try:
            response = requests.get(
                'http://api.weatherapi.com/v1/current.json', 
                params=self.parameters,
                timeout=4,
                )
        except requests.exceptions.RequestException as e:
            print(f"\033[31mNetwork error: {e}\033[0m")
            return None

        if response.status_code == 200: return response

        if response.status_code == 400: 
            print('\033[31mLocation not found!\033[0m')
            return None
        print(f'\033[31mError. Please try again.\033[0m')
        return None

    def treating_response(self, response) -> ClimateInfo:
        data = response.json()
        print(data)
        location = data.get("location", {})
        current = data.get("current", {})

        country = location.get("country", "Unknown")
        city_name = location.get("name", "Unknown")
        region = location.get("region", "Unknown")
        update_time = current.get("last_updated")
        if " " in update_time:
            date, hour = update_time.split(" ")
        else:
            date, hour = "", ""
        condition = current.get("condition", {}).get("text", "Unknown")
        chance_of_rain = current.get("chance_of_rain", None)
        feels_like = current.get("feelslike_c", None)
        humidity = current.get("humidity", None)
        temperature = current.get("temp_c", None)
        winds = current.get("wind_kph", None)
    
        return ClimateInfo(
            date=date, hour=hour, condition=condition,chance_of_rain=chance_of_rain,feels_like=feels_like,humidity=humidity,
                        temperature=temperature, winds=winds, country=country, city_name=city_name, region=region
        )

class Menu:
    def print_menu(self, climate_info: ClimateInfo) -> None:
        print(f'City: {climate_info.city_name}')
        print(f'Region: {climate_info.region}')
        print(f'Country: {climate_info.country}\n')
        print(f'Date: {climate_info.date}')
        print(f'Hour: {climate_info.hour}\n')
        print(f'Chance of rain: {climate_info.chance_of_rain}%')
        print(f'Humidity: {climate_info.humidity}')
        print(f'Winds: {climate_info.winds} km/h\n')
        print(f'Condition: {climate_info.condition}')
        print(f'Current temperature: {climate_info.temperature}°C')
        print(f'Feels like {climate_info.feels_like}°C\n')

class User:

    def get_city(self) -> str:
        city = self.__validate_city()
        return city

    def __validate_city(self) -> str:
        while True:
            try:
                city = str(input("Which city are you looking to get the climate info? ")).strip()
                if len(city) < 2: raise IndexError()
                allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ,-'")
                if all(letter in allowed_chars for letter in city): return city
                raise IndexError()
            except IndexError:
                print('\033[31mInvalid city! Please insert a valid location.\033[0m')