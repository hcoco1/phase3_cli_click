# Standard library imports
import datetime
import logging
import os
import random
import sys
import time
from io import StringIO
# Third-party library imports
from prettytable import PrettyTable
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from termcolor import colored
import pyfiglet
import requests

# Application/library specific imports
from start import start
from weather import get_weather
from game import play_game, save_user_score, display_user_scores
from db.seed import session
from db.data import states_to_play
from display import (
    display_states,
    display_counties,
    display_cities,
    display_facilities,
    display_entity,
)
from helpers import (
    add_single_entity,
    update_city_coordinates,
    update_entity_attribute,
    delete_entity_by_name,
    print_animated_text
)
from db.models import State, City, County
# Constants
INVALID_CHOICE_MESSAGE = pyfiglet.figlet_format("Invalid choice. Please try again.")
GOODBYE_MESSAGE = pyfiglet.figlet_format("Goodbye!")

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
            # display_facilities(session)

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
