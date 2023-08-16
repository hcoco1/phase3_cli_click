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
from lib.db.data import states_to_play
from termcolor import colored
import datetime
import pyfiglet
import random
import requests
import time
from dotenv import load_dotenv

# Constants
INVALID_CHOICE_MESSAGE = pyfiglet.figlet_format("Invalid choice. Please try again.")
GOODBYE_MESSAGE = pyfiglet.figlet_format("Goodbye!")

def print_animated_text(text, delay=0.1):
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        
    
#print_animated_text("Hello World!")


def start():
    """Initiate the program and get user's name."""
    ascii_banner = pyfiglet.figlet_format("Database Tool!")
    print_animated_text(ascii_banner, 0.004)
    print_animated_text(colored("Please enter your name (or type 'exit' to quit): \n", "blue"))
    user_name = input()
    if user_name.lower() == "exit":
        print(GOODBYE_MESSAGE)
        sys.exit()  # Exit the entire app

    print(colored(f"Hello {user_name}!", "magenta"))
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("user_details.txt", "a") as file:
        file.write(f"{user_name}, {current_datetime}\n")
    
    print_animated_text(colored("Your name was saved successfully in our local storage!\n", "red"))
    return user_name


def test_db(user_name):
    print("Testing the Database")
    # Add your database testing logic here
    entity_map = {
        "5": {"type": State, "name": "state"},
        "6": {"type": City, "name": "city"},
        "7": {"type": County, "name": "county"},
    }
    while True:
        print(colored("\nChoose a CRUD operation:", "red"))
        print(colored("1. Show US states, cities, and counties", "yellow"))
        print(colored("2. Add a new US Entity (State/City/County)", "yellow"))
        print(colored("3. Update an US Entity (State/City/County)", "yellow"))
        print(colored("4. Delete an US Entity (State/City/County)", "yellow"))
        print(colored("5. Exit", "yellow"))

        choice = input(colored("Enter your choice: ", "red"))

        if choice == "1":
            display_states(session)
            display_counties(session)
            display_cities(session)
            display_facilities(session)

        elif choice == "2":
            print(colored("\nChoose an entity to add:", "red"))
            print(colored("a. State", "yellow"))
            print(colored("b. City", "yellow"))
            print(colored("c. County", "yellow"))

            entity_choice = input(colored("Enter your choice (a/b/c): ", "blue"))
            if entity_choice == "a":
                entity_type = State
                extra_ops = []
            elif entity_choice == "b":
                entity_type = City
                extra_ops = [update_city_coordinates, get_weather]
            elif entity_choice == "c":
                entity_type = County
                extra_ops = []

            name = input(colored(f"Enter {entity_type.__name__.lower()} name: ", "blue")).strip().lower()
            add_single_entity(session, entity_type=entity_type, name=name.title(), population=0, area=0)
            for operation in extra_ops:
                if operation == update_city_coordinates:
                    operation(city_name=name.title())
                elif operation == get_weather:
                    print(operation(name.title()))

            display_entity(session, entity_type=entity_type, entity_name=name.title())


        elif choice == "3":
            print(colored("\nChoose an entity to update:", "red"))
            print(colored("a. State", "yellow"))
            print(colored("b. City", "yellow"))
            print(colored("c. County", "yellow"))

            entity_choice = input(colored("Enter your choice: ", "blue")).lower()

            entity_map = {
                "a": {"type": State, "name": "state"},
                "b": {"type": City, "name": "city"},
                "c": {"type": County, "name": "county"},
            }

            if entity_choice in entity_map:
                entity_type = entity_map[entity_choice]["type"]
                entity_name_input = input(
                    colored(f"Enter the name of the {entity_map[entity_choice]['name']} to modify: ", "blue")
                ).strip().lower()
                attribute = input(colored("Enter the attribute to modify: ", "blue")).strip().lower()
                new_value = input(colored("Enter the new value: ", "blue")).strip().lower()

                update_entity_attribute(
                    session,
                    entity_type=entity_type,
                    entity_name=entity_name_input.title(),
                    attribute=attribute,
                    new_value=new_value,
                )
                display_entity(session, entity_type=entity_type, entity_name=entity_name_input.title())
            else:
                print(colored("Invalid choice!", "red"))


        elif choice == "4":
            print(colored("\nChoose an entity to delete:", "red"))
            print(colored("a. State", "yellow"))
            print(colored("b. County", "yellow"))
            print(colored("c. City", "yellow"))
            
            sub_choice = input(colored("Enter your choice: ", "blue"))
            
            entity_map = {
                "a": {"type": State, "name": "state", "display": display_states},
                "b": {"type": County, "name": "county", "display": display_counties},
                "c": {"type": City, "name": "city", "display": display_cities}
            }
            
            if sub_choice in entity_map:
                entity_name = input(colored(f"Enter {entity_map[sub_choice]['name']} name to delete: ", "blue")).strip()
                delete_entity_by_name(
                    session,
                    entity_name=entity_name.title(),
                    entity_cls=entity_map[sub_choice]['type'],
                )
                entity_map[sub_choice]['display'](session)
            else:
                print(colored("Invalid choice!", "red"))





        elif choice == "5":
            print(colored("Redirecting to the main Menu!", "magenta"))
            break

        else:
            ascii_banner = pyfiglet.figlet_format("Invalid choice. Please try again.")
            print(ascii_banner)


def play_game(session):
    print("-" * len("Welcome to the Capital City Guessing Game!"))
    print(colored("Welcome to the Capital City Guessing Game!", "green"))
    print("-" * len("Welcome to the Capital City Guessing Game!"))
    
    print_animated_text(colored("Try to guess the capital city of each U.S. state. ", "blue"))
    print_animated_text(colored("Type 'exit' anytime to quit the game.\n", "blue"))
    
    start_time = datetime.datetime.now()

    correct_guesses = 0

    for _ in range(5):  # Loop for exactly 5 questions
        state = random.choice(states_to_play)  # Choose a random state
        state_name = state['name']

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

        if capital_guess == state['capital'].lower():
            print(colored("Correct!", "green"))
            correct_guesses += 1
        else:
            print(colored(f"Oops! The correct answer is {state['capital']}.", "red"))

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


def main():
    while True:
        user_name = start()
        while True:
            print(colored("\nChoose an option:", "red"))
            print(colored("1. Manage the database", "yellow"))
            print(colored("2. Play CapitalStates game", "yellow"))
            print(colored("3. Weather info for every city in the world", "yellow"))  # New Option
            print(colored("4. Exit", "yellow"))

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
                display_user_scores()

            elif choice == "3":
                city_to_check = input(colored("Enter the city name: ", "blue")).strip()
                print(get_weather(city_to_check))

            elif choice == "4":
                print(GOODBYE_MESSAGE)
                sys.exit()  # Exit the entire app
            else:
                print(INVALID_CHOICE_MESSAGE)


if __name__ == "__main__":
    main()
