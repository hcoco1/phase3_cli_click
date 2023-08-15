import sys

sys.path.append("/home/hcoco1/Development/code/phase-3/phase3_cli_click")
import os

base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_path)

from lib.db.models import State, City, County
from lib.db.seed import session
from lib.db.display import (
    display_states,
    display_counties,
    display_cities,
    display_facilities,
    display_entity,
)
from lib.helpers import (
    add_single_entity,
    update_city_coordinates,
    update_entity_attribute,
    delete_entity_by_name,
)
from termcolor import colored
import datetime
import pyfiglet
import random
import requests


# Constants
INVALID_CHOICE_MESSAGE = pyfiglet.figlet_format("Invalid choice. Please try again.")
GOODBYE_MESSAGE = pyfiglet.figlet_format("Goodbye!")


def start():
    """Initiate the program and get user's name."""
    ascii_banner = pyfiglet.figlet_format("Database Tool!")
    print(ascii_banner)
    user_name = input(
        colored("Please enter your name (or type 'exit' to quit): ", "blue")
    )
    if user_name.lower() == "exit":
        print(GOODBYE_MESSAGE)
        sys.exit()  # Exit the entire app

    print(colored(f"Hello {user_name}!", "magenta"))
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("user_details.txt", "a") as file:
        file.write(f"{user_name}, {current_datetime}\n")
    print(colored(f"Your name was saved successfully in our local storage!", "red"))
    return user_name


def test_db(user_name):
    print("Testing the Database")
    # Add your database testing logic here

    while True:
        print(colored("\nChoose a CRUD operation:", "red"))
        print(colored("1. Show the DataBase", "yellow"))
        print(colored("2. Add a new State", "yellow"))
        print(colored("3. Add a new City", "yellow"))
        print(colored("4. Add a new County", "yellow"))
        print(colored("5. Update a State", "yellow"))
        print(colored("6. Update a City", "yellow"))
        print(colored("7. Update a County", "yellow"))
        print(colored("8. Delete a State", "yellow"))
        print(colored("9. Delete a County", "yellow"))
        print(colored("10. Delete a City", "yellow"))
        print(colored("11. Exit", "yellow"))

        choice = input(colored("Enter your choice: ", "red"))

        if choice == "1":
            display_states(session)
            display_counties(session)
            display_cities(session)
            display_facilities(session)

        elif choice == "2":
            name = input(colored("Enter state name: ", "blue")).strip().lower()
            add_single_entity(
                session, entity_type=State, name=name.title(), population=0, area=0
            )
            display_entity(session, entity_type=State, entity_name=name.title())

        elif choice == "3":
            name = input(colored("Enter city name: ", "blue")).strip().lower()
            add_single_entity(
                session, entity_type=City, name=name.title(), population=0, area=0
            )
            update_city_coordinates(city_name=name.title())
            display_entity(session, entity_type=City, entity_name=name.title())
            print(get_weather(name.title()))

        elif choice == "4":
            name = input(colored("Enter county name: ", "blue")).strip().lower()
            add_single_entity(
                session, entity_type=County, name=name.title(), population=0, area=0
            )
            display_entity(session, entity_type=County, entity_name=name.title())

        elif choice == "5":
            entity_name = (
                input(colored("Enter the name of the state to modify: ", "blue"))
                .strip()
                .lower()
            )
            attribute = (
                input(colored("Enter the attribute to modify: ", "blue"))
                .strip()
                .lower()
            )
            new_value = input(colored("Enter the new value: ", "blue")).strip().lower()
            update_entity_attribute(
                session,
                entity_type=State,
                entity_name=entity_name.title(),
                attribute=attribute,
                new_value=new_value,
            )
            display_entity(session, entity_type=State, entity_name=entity_name.title())

        elif choice == "6":
            entity_name = (
                input(colored("Enter the name of the city to modify: ", "blue"))
                .strip()
                .lower()
            )
            attribute = (
                input(colored("Enter the attribute to modify: ", "blue"))
                .strip()
                .lower()
            )
            new_value = input(colored("Enter the new value: ", "blue")).strip().lower()
            update_entity_attribute(
                session,
                entity_type=City,
                entity_name=entity_name.title(),
                attribute=attribute,
                new_value=new_value,
            )
            display_entity(session, entity_type=City, entity_name=entity_name.title())

        elif choice == "7":
            entity_name = (
                input(colored("Enter the name of the county to modify: ", "blue"))
                .strip()
                .lower()
            )
            attribute = (
                input(colored("Enter the attribute to modify: ", "blue"))
                .strip()
                .lower()
            )
            new_value = input(colored("Enter the new value: ", "blue")).strip().lower()
            update_entity_attribute(
                session,
                entity_type=County,
                entity_name=entity_name.title(),
                attribute=attribute,
                new_value=new_value,
            )
            display_entity(session, entity_type=County, entity_name=entity_name.title())

        elif choice == "8":
            entity_name = input(colored("Enter state name to delete: ", "blue"))
            delete_entity_by_name(
                session,
                entity_name=entity_name,
                entity_cls=State,
            )
            display_states(session)

        elif choice == "9":
            entity_name = input(colored("Enter county name to delete: ", "blue"))
            delete_entity_by_name(
                session,
                entity_name=entity_name.title(),
                entity_cls=County,
            )
            display_counties(session)

        elif choice == "10":
            entity_name = input(colored("Enter city name to delete: ", "blue"))
            delete_entity_by_name(
                session,
                entity_name=entity_name.title(),
                entity_cls=City,
            )
            display_cities(session)

        elif choice == "11":
            print(colored("Redirecting to the main Menu!", "magenta"))
            break

        else:
            ascii_banner = pyfiglet.figlet_format("Invalid choice. Please try again.")
            print(ascii_banner)


def play_game(session):
    states = session.query(State).all()
    print("-" * len("Welcome to the Capital City Guessing Game!"))
    print(colored("Welcome to the Capital City Guessing Game!", "green"))
    print("-" * len("Welcome to the Capital City Guessing Game!"))
    print("Try to guess the capital city of each U.S. state.")
    print("Type 'exit' anytime to quit the game.\n")
    # print("-" * len("Welcome to the Capital City Guessing Game!"))

    start_time = datetime.datetime.now()

    correct_guesses = 0

    for _ in range(5):  # Loop for exactly 10 questions
        state = random.choice(states)  # Choose a random state
        state_name = state.name

        capital_guess = (
            input(colored(f"What is the capital city of {state_name}? ", "yellow"))
            .strip()
            .lower()
        )

        if capital_guess == "exit":
            print(
                colored(
                    f"Thanks for playing! You guessed {correct_guesses}/5 capitals correctly.",
                    "green",
                )
            )
            break

        if capital_guess == state.capital.lower():
            print(colored("Correct!", "green"))
            correct_guesses += 1
        else:
            print(colored(f"Oops! The correct answer is {state.capital}.", "red"))

    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time

    print(
        colored(
            f"Thanks for playing! You guessed {correct_guesses}/5 capitals correctly.",
            "green",
        )
    )
    print(f"You took {elapsed_time.total_seconds():.2f} seconds to answer 5 questions.")

    return correct_guesses, elapsed_time.total_seconds()  # Return the results


def save_user_score(name, score, time_taken, correct_answers):
    with open("user_scores.txt", "a") as file:
        file.write(f"{name},{score},{time_taken},{correct_answers}\n")


def read_user_scores():
    data = []
    with open("user_scores.txt", "r") as file:
        content = file.read().strip()
        if not content:  # Check if the content is empty or whitespace
            return data  # Return an empty list

        for line in content.splitlines():
            parts = line.split(",")
            if len(parts) != 4:
                print(f"Warning: Ignored malformed line in user_scores.txt: {line}")
                continue

            name, score, time_taken, correct_answers = parts

            # Check if score and correct_answers are integers
            if not score.isdigit() or not correct_answers.isdigit():
                print(
                    f"Warning: Ignored line with non-integer score or answers in user_scores.txt: {line}"
                )
                continue

            data.append(
                {
                    "name": name,
                    "score": int(score),
                    "time": time_taken,
                    "correct_answers": int(correct_answers),
                }
            )
    return data


from prettytable import PrettyTable


def display_user_scores():
    data = read_user_scores()
    table = PrettyTable()
    table.field_names = ["Name", "Score", "Time", "Correct Answers"]

    for record in data:
        table.add_row(
            [record["name"], record["score"], record["time"], record["correct_answers"]]
        )
    print("-" * len("User's Scores"))
    print("User's Scores")
    print("-" * len("User's Scores"))

    print(table)


import logging
import sys
from io import StringIO
import requests
from lib.db.data import weather_icons


font_options = [
    "standard",
    "slant",
    "3-d",
    "block",
    "bubble",
    "digital",
    "lean",
    "mini",
    "script",
    "shadow",
    "smscript",
    "smslant",
    "small",
    "soft",
    "tombstone",
]
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Get the API_KEY from environment variables
API_KEY = os.getenv("API_KEY")
# Now you can use the API_KEY in your script
print(
    API_KEY
)  # Just for demonstration, avoid printing sensitive info in real applications


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


def main():
    while True:
        user_name = start()
        while True:
            print(colored("\nChoose an option:", "red"))
            print(colored("1. Test the database", "yellow"))
            print(colored("2. Play a game", "yellow"))
            print(colored("3. Display Scores", "yellow"))  # New Option
            print(colored("4. Get Weather", "yellow"))  # New Option
            print(colored("5. Exit", "yellow"))

            choice = input(colored("Enter your choice: ", "red"))

            if choice == "1":
                test_db(user_name)
            elif choice == "2":
                score, time_taken = play_game(session)
                save_user_score(
                    name=user_name,
                    score=score,
                    time_taken=time_taken,
                    correct_answers=score,
                )
            elif choice == "3":
                display_user_scores()

            elif choice == "4":
                city_to_check = input(colored("Enter the city name: ", "blue")).strip()
                print(get_weather(city_to_check))

            elif choice == "5":
                print(GOODBYE_MESSAGE)
                sys.exit()  # Exit the entire app
            else:
                print(INVALID_CHOICE_MESSAGE)


if __name__ == "__main__":
    main()
