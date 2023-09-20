# Weather App

This is a simple Python program that allows users to retrieve and display current weather information for a specified city or location. It uses the OpenWeatherMap API to fetch weather data and provides details such as temperature, humidity, description, and wind speed.

## Features

- Fetches current weather data based on user input.
- Displays temperature in Celsius.
- Provides information on humidity, weather description, and wind speed.
- Handles errors gracefully, such as incorrect user input or API request issues.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- Internet connection to make API requests.
- OpenWeatherMap API key. (You can obtain one by signing up at https://openweathermap.org/api)

## Usage
   To use this Weather App, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/Ennin-Wilson/weather.git


1. **Configure API Key**: Open the weather.py file and replace 'your-api-key' with your actual OpenWeatherMap API key
   
2. **Run the Program**:Execute the following command to run the program:
   ``` bash
   python weather.py

3. **Enter Location**: Enter the name of the city or location for which you want to retrieve weather information.

4. **View Weather Details**: The program will display the current weather details, including temperature, humidity, weather description, and wind speed.

## Error Handling
This Weather App includes error handling for the following scenarios:

1. **Invalid Input**: If you enter a numeric value or an invalid location, the program will exit and display an error message.

2. **API Request Failure**: If the API request fails due to network issues or other problems, the program will exit and provide an error message.

## Acknowledgments
This project uses the OpenWeatherMap API to retrieve weather data. You can learn more about their API [here](https://openweathermap.org/api).
