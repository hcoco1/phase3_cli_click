import datetime
import random
import time # For sleep function
from termcolor import colored
from pyfiglet import figlet_format
from prettytable import PrettyTable
from helpers import print_animated_text
from db.data import states_to_add





def play_game(session):
    print("-" * len("Welcome to the Capital City Guessing Game!"))
    print(colored("Welcome to the Capital City Guessing Game!", "green"))
    print("-" * len("Welcome to the Capital City Guessing Game!"))
    print_animated_text(colored("Try to guess the capital city of each U.S. state. ", "blue"))
    print_animated_text(colored("Type 'exit' anytime to quit the game.\n", "blue"))
    start_time = datetime.datetime.now()
    correct_guesses = 0
    for _ in range(5):  # Loop for exactly 5 questions
        state = random.choice(states_to_add)  # Choose a random state
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