import datetime
import random
from termcolor import colored
from pyfiglet import figlet_format
from prettytable import PrettyTable
from lib.helpers import print_animated_text
from lib.db.models import State




def play_game(session):
    print("-" * len("Welcome to the Capital City Guessing Game!"))
    print(colored("Welcome to the Capital City Guessing Game!", "green"))
    print("-" * len("Welcome to the Capital City Guessing Game!"))
    print_animated_text(colored("Try to guess the capital city of each U.S. state. ", "blue"))
    print_animated_text(colored("Type 'exit' anytime to quit the game.\n", "blue"))
    start_time = datetime.datetime.now()
    correct_guesses = 0
    for _ in range(2):  # Loop for exactly 5 questions
        state = random.choice(states_to_play)  # Choose a random state
        state_name = state.name
        capital_guess = (
            input(colored(f"What is the capital city of {state_name}? ", "yellow"))
            .strip()
            .lower()
        )

        if capital_guess == "exit":
            print(
                colored(
                    f"Thanks for playing! You guessed {correct_guesses}/2 capitals correctly.",
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
            f"Thanks for playing! You guessed {correct_guesses}/2 capitals correctly.",
            "green",
        )
    )
    print(f"You took {elapsed_time.total_seconds():.2f} seconds to answer 2 questions.")

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
    
states_to_play = [
    State(
        name="Alabama",
        abbreviation="AL",
        population=4903185,
        capital="Montgomery",
        area=52420,
    ),
    State(
        name="Alaska",
        abbreviation="AK",
        population=731545,
        capital="Juneau",
        area=665384,
    ),
    State(
        name="Arizona",
        abbreviation="AZ",
        population=7278717,
        capital="Phoenix",
        area=113990,
    ),
    State(
        name="Arkansas",
        abbreviation="AR",
        population=3017804,
        capital="Little Rock",
        area=53179,
    ),
    State(
        name="California",
        abbreviation="CA",
        population=39538223,
        capital="Sacramento",
        area=163695,
    ),
    State(
        name="Colorado",
        abbreviation="CO",
        population=5773714,
        capital="Denver",
        area=104094,
    ),
    State(
        name="Connecticut",
        abbreviation="CT",
        population=3565287,
        capital="Hartford",
        area=5543,
    ),
    State(
        name="Delaware",
        abbreviation="DE",
        population=973764,
        capital="Dover",
        area=2489,
    ),
    State(
        name="Florida",
        abbreviation="FL",
        population=21538187,
        capital="Tallahassee",
        area=65758,
    ),
    State(
        name="Georgia",
        abbreviation="GA",
        population=10617423,
        capital="Atlanta",
        area=59425,
    ),
    State(
        name="Hawaii",
        abbreviation="HI",
        population=1455271,
        capital="Honolulu",
        area=10932,
    ),
    State(
        name="Idaho", abbreviation="ID", population=1787065, capital="Boise", area=83569
    ),
    State(
        name="Illinois",
        abbreviation="IL",
        population=12671821,
        capital="Springfield",
        area=57914,
    ),
    State(
        name="Indiana",
        abbreviation="IN",
        population=6732219,
        capital="Indianapolis",
        area=36420,
    ),
    State(
        name="Iowa",
        abbreviation="IA",
        population=3155070,
        capital="Des Moines",
        area=56273,
    ),
    State(
        name="Kansas",
        abbreviation="KS",
        population=2913314,
        capital="Topeka",
        area=82278,
    ),
    State(
        name="Kentucky",
        abbreviation="KY",
        population=4467673,
        capital="Frankfort",
        area=40408,
    ),
    State(
        name="Louisiana",
        abbreviation="LA",
        population=4648794,
        capital="Baton Rouge",
        area=52378,
    ),
    State(
        name="Maine",
        abbreviation="ME",
        population=1344212,
        capital="Augusta",
        area=35380,
    ),
    State(
        name="Maryland",
        abbreviation="MD",
        population=6045680,
        capital="Annapolis",
        area=12406,
    ),
    State(
        name="Massachusetts",
        abbreviation="MA",
        population=6892503,
        capital="Boston",
        area=10554,
    ),
    State(
        name="Michigan",
        abbreviation="MI",
        population=9986857,
        capital="Lansing",
        area=96714,
    ),
    State(
        name="Minnesota",
        abbreviation="MN",
        population=5639632,
        capital="Saint Paul",
        area=86936,
    ),
    State(
        name="Mississippi",
        abbreviation="MS",
        population=2976149,
        capital="Jackson",
        area=48432,
    ),
    State(
        name="Missouri",
        abbreviation="MO",
        population=6137428,
        capital="Jefferson City",
        area=69707,
    ),
    State(
        name="Montana",
        abbreviation="MT",
        population=1068778,
        capital="Helena",
        area=147040,
    ),
    State(
        name="Nebraska",
        abbreviation="NE",
        population=1934408,
        capital="Lincoln",
        area=77348,
    ),
    State(
        name="Nevada",
        abbreviation="NV",
        population=3080156,
        capital="Carson City",
        area=110572,
    ),
    State(
        name="New Hampshire",
        abbreviation="NH",
        population=1359711,
        capital="Concord",
        area=9349,
    ),
    State(
        name="New Jersey",
        abbreviation="NJ",
        population=8882190,
        capital="Trenton",
        area=8723,
    ),
    State(
        name="New Mexico",
        abbreviation="NM",
        population=2117522,
        capital="Santa Fe",
        area=121590,
    ),
    State(
        name="New York",
        abbreviation="NY",
        population=19453561,
        capital="Albany",
        area=54555,
    ),
    State(
        name="North Carolina",
        abbreviation="NC",
        population=10488084,
        capital="Raleigh",
        area=53819,
    ),
    State(
        name="North Dakota",
        abbreviation="ND",
        population=762062,
        capital="Bismarck",
        area=70698,
    ),
    State(
        name="Ohio",
        abbreviation="OH",
        population=11689100,
        capital="Columbus",
        area=44826,
    ),
    State(
        name="Oklahoma",
        abbreviation="OK",
        population=3956971,
        capital="Oklahoma City",
        area=69903,
    ),
    State(
        name="Oregon",
        abbreviation="OR",
        population=4217737,
        capital="Salem",
        area=98379,
    ),
    State(
        name="Pennsylvania",
        abbreviation="PA",
        population=12801989,
        capital="Harrisburg",
        area=46054,
    ),
    State(
        name="Rhode Island",
        abbreviation="RI",
        population=1059361,
        capital="Providence",
        area=1545,
    ),
    State(
        name="South Carolina",
        abbreviation="SC",
        population=5148714,
        capital="Columbia",
        area=32020,
    ),
    State(
        name="South Dakota",
        abbreviation="SD",
        population=884659,
        capital="Pierre",
        area=77116,
    ),
    State(
        name="Tennessee",
        abbreviation="TN",
        population=6829174,
        capital="Nashville",
        area=42144,
    ),
    State(
        name="Texas",
        abbreviation="TX",
        population=28995881,
        capital="Austin",
        area=268596,
    ),
    State(
        name="Utah",
        abbreviation="UT",
        population=3271616,
        capital="Salt Lake City",
        area=84897,
    ),
    State(
        name="Vermont",
        abbreviation="VT",
        population=623989,
        capital="Montpelier",
        area=9616,
    ),
    State(
        name="Virginia",
        abbreviation="VA",
        population=8535519,
        capital="Richmond",
        area=42775,
    ),
    State(
        name="Washington",
        abbreviation="WA",
        population=7614893,
        capital="Olympia",
        area=71298,
    ),
    State(
        name="West Virginia",
        abbreviation="WV",
        population=1792147,
        capital="Charleston",
        area=24230,
    ),
    State(
        name="Wisconsin",
        abbreviation="WI",
        population=5822434,
        capital="Madison",
        area=65496,
    ),
    State(
        name="Wyoming",
        abbreviation="WY",
        population=578759,
        capital="Cheyenne",
        area=97813,
    ),
]