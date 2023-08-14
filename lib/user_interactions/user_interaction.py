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
)
from lib.helpers import (
    add_single_state,
    add_single_city,
    add_single_county,
    update_city_coordinates,
    update_entity_attribute,
    delete_entity_by_name,
)
from termcolor import colored
import datetime
import pyfiglet
import datetime
import random


def start():
    ascii_banner = pyfiglet.figlet_format("Database Tool!")
    print(ascii_banner)
    # Ask the user for their name
    user_name = input(
        colored("Please enter your name (or type 'exit' to quit): ", "blue")
    )
    if user_name.lower() == "exit":
        print(pyfiglet.figlet_format("Goodbye!!!"))
        sys.exit()  # Exit the entire app

    ascii_banner = pyfiglet.figlet_format(f"Hello {user_name}!")
    print(ascii_banner)
    # Get the current date and time
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Open a text file in append mode and save the details
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
            add_single_state(session, name.title(), population=0, area=0)

        elif choice == "3":
            name = input(colored("Enter city name: ", "blue")).strip().lower()
            add_single_city(session, name.title(), population=0, area=0)
            update_city_coordinates()

        elif choice == "4":
            name = input(colored("Enter county name: ", "blue")).strip().lower()
            add_single_county(session, name.title(), population=0, area=0)

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
                entity_cls=State,
                entity_name=entity_name.title(),
                attribute=attribute,
                new_value=new_value,
            )

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
                entity_cls=City,
                entity_name=entity_name.title(),
                attribute=attribute,
                new_value=new_value,
            )

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
                entity_cls=County,
                entity_name=entity_name.title(),
                attribute=attribute,
                new_value=new_value,
            )

        elif choice == "8":
            entity_name = (
                input(colored("Enter state name to delete: ", "blue")).strip().lower()
            )
            delete_entity_by_name(
                session,
                entity_name=entity_name.title(),
                entity_cls=State,
            )

        elif choice == "9":
            entity_name = (
                input(colored("Enter county name to delete: ", "blue")).strip().lower()
            )
            delete_entity_by_name(
                session,
                entity_name=entity_name.title(),
                entity_cls=County,
            )

        elif choice == "10":
            entity_name = (
                input(colored("Enter city name to delete: ", "blue")).strip().lower()
            )
            delete_entity_by_name(
                session,
                entity_name=entity_name.title(),
                entity_cls=City,
            )

        elif choice == "11":
            ascii_banner = pyfiglet.figlet_format(f"Goodbye {user_name}!!!")
            print(ascii_banner)
            break

        else:
            ascii_banner = pyfiglet.figlet_format("Invalid choice. Please try again.")
            print(ascii_banner)




def play_game(session):
    states = session.query(State).all()

    print(colored("Welcome to the Capital City Guessing Game!", "green"))
    print("Try to guess the capital city of each U.S. state.")
    print("Type 'exit' anytime to quit the game.\n")

    start_time = datetime.datetime.now()

    correct_guesses = 0

    for _ in range(10):  # Loop for exactly 10 questions
        state = random.choice(states)  # Choose a random state
        state_name = state.name
        capital_guess = input(f"What is the capital city of {state_name}? ").strip().lower()

        if capital_guess == "exit":
            print(colored(f"Thanks for playing! You guessed {correct_guesses}/10 capitals correctly.", "green"))
            break
        
        if capital_guess == state.capital.lower():
            print(colored("Correct!", "green"))
            correct_guesses += 1
        else:
            print(colored(f"Oops! The correct answer is {state.capital}.", "red"))

    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time

    print(colored(f"Thanks for playing! You guessed {correct_guesses}/10 capitals correctly.", "green"))
    print(f"You took {elapsed_time.total_seconds():.2f} seconds to answer 10 questions.")



def main():
    while True:
        user_name = start()
        if user_name is None:
            break  # Exit if the user wants to quit

        while True:
            print(colored("\nChoose an option:", "red"))
            print(colored("1. Test the database", "yellow"))
            print(colored("2. Play a game", "yellow"))
            print(colored("3. Exit", "yellow"))

            choice = input(colored("Enter your choice: ", "red"))

            if choice == "1":
                test_db(user_name)

            elif choice == "2":
                play_game()

            elif choice == "3":
                ascii_banner = pyfiglet.figlet_format(f"Goodbye!")
                print(ascii_banner)
                sys.exit()  # Exit the entire app

            elif choice == "11":
                ascii_banner = pyfiglet.figlet_format("Goodbye!")
                print(ascii_banner)
                sys.exit()  # Exit the entire app

            else:
                ascii_banner = pyfiglet.figlet_format(
                    "Invalid choice. Please try again."
                )
                print(ascii_banner)


if __name__ == "__main__":
    main()
