import requests
import json
from sys import exit


# my api key
api_key = ""  # ||Add API KEY||


def main():
    return weather_app()


def weather_app():
    user_input = input("Enter city or location: ")

    if user_input.isdigit():
        exit("MUST BE A CITY OR LOCATION NOT A NUMBER!")
    else:
        try:
            respons = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=metric"
            )
            if respons.status_code == 200:
                json_data = respons.json()
                if "weather" in json_data and json_data["weather"]:
                    weather_description = json_data["weather"][0]["description"]
                    temperature = json_data["main"]["temp"]
                    humidity = json_data["main"]["humidity"]
                    wind_speed = json_data["wind"]["speed"]
                    location_name = json_data["name"]

                    print(f"Weather in {location_name}")
                    print(f"Temperature: {temperature:.2f}˚C")
                    print(f"Humidity: {humidity}%")
                    print(f"Description: {weather_description}")
                    print(f"Wind Speed: {wind_speed} Km/h")
                else:
                    print("Weather data is incomplete. Please try again later.")
            else:
                print("City or Location not found. Please check your input.")

        except requests.RequestException as e:
            exit(f"An error occurred: {e}")


print(main())
