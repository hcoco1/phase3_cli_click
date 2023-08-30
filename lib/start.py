import sys
import datetime
import pyfiglet
from termcolor import colored
from lib.helpers import print_animated_text


GOODBYE_MESSAGE = pyfiglet.figlet_format("Goodbye!")

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