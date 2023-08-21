import pyfiglet
import os
from db.data import weather_icons
from io import StringIO
from termcolor import colored
import logging
import requests
import sys
from dotenv import load_dotenv




load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_weather(cityname):
    # Set the logging level of urllib3 to CRITICAL to suppress debug messages
    logging.getLogger("urllib3").setLevel(logging.CRITICAL)

    url = f"http://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={API_KEY}&units=imperial"

    try:
        # Redirect stdout to a temporary buffer
        old_stdout = sys.stdout
        sys.stdout = StringIO()

        response = requests.get(url)
        data = response.json()

        # Restore the original stdout and get captured output
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout

        if response.status_code == 404:
            return f"City '{cityname}' not found."
        elif response.status_code == 401:
            return "Invalid API key. Please check your API key."
        elif response.status_code != 200:
            return f"An error occurred: {data.get('message', 'Unknown error')}"

        temperature = data["main"]["temp"]
        weather_status = data["weather"][0]["description"]
        weather_icon = weather_icons.get(weather_status.lower(), "❓")

        # Stylize and colorize the city name using pyfiglet
        city_banner = pyfiglet.figlet_format(cityname.title(), font="standard")
        city_colored = colored(city_banner, "blue")
       

        # Construct the final message with color and stylized city name
        final_message = (
            f"\nWeather in \n {city_colored} {temperature:.1f}°C, "
            f"{weather_icon}   {weather_status.capitalize()}\n"
        )
       

        # Append the captured output before the actual output
        return f"{output}{final_message}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"