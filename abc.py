#Create a command-line tool that accepts a city's name and returns the current weather forecast. Leverage OpenWeatherMap API to fetch weather data and parse it using Python. 
import requests
import json
import sys
#function to get the weather data from the API
def get_data(city):
    api_key = "b27834f0c0f0b1eb7720d117f8b61033"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
     # Send GET request to OpenWeatherMap API with specified parameters
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
         # Convert response to JSON
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    # handling Failed to parse response error
    except (KeyError, json.JSONDecodeError) as err:
        print(f"Failed to parse response: {err}")
        sys.exit(1)
#function to display weather data
def display_data(weather_data):
    print(f"Current weather in {weather_data['name']}:")
    print(f"{weather_data['weather'][0]['main']}: {weather_data['weather'][0]['description']}")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Feels like: {weather_data['main']['feels_like']}°C")
    print(f"Minimum temperature: {weather_data['main']['temp_min']}°C")
    print(f"Maximum temperature: {weather_data['main']['temp_max']}°C")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Wind speed: {weather_data['wind']['speed']} m/s")
#main function
# Get city name from command line arguments
def main():
    if len(sys.argv) < 2:
        print("Please provide city name as command line argument")
        sys.exit(1)
    city = sys.argv[1]
    weather_data = get_data(city)
    display_data(weather_data) 
if __name__ == "__main__":
    main()       
        



          

 