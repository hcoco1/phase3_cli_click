# Standard library imports
import sys

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
from test_db import test_db, session
from helpers import print_animated_text

# Constants
INVALID_CHOICE_MESSAGE = pyfiglet.figlet_format("Invalid choice. Please try again.")
GOODBYE_MESSAGE = pyfiglet.figlet_format("Goodbye!")


def main():
    while True:
        user_name = start()
        while True:
            print(colored("\nChoose an option:", "red"))
            print(colored("1. Manage the database", "yellow"))
            print(colored("2. Play CapitalStates game", "yellow"))
            print(
                colored("3. Weather info for every city in the world", "yellow")
            )  # New Option
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
                print_animated_text(get_weather(city_to_check), 0.004)

            elif choice == "4":
                print(GOODBYE_MESSAGE)
                sys.exit()  # Exit the entire app
            else:
                print("Invalid choice. Please try again.")




if __name__ == "__main__":
    main()
