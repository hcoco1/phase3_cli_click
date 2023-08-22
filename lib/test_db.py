import pyfiglet
from sqlalchemy import func
from termcolor import colored
from db.models import State, City, County
from display import (
    display_states,
    display_counties,
    display_cities,
    display_facilities,
    display_entity,
)
from helpers import (
    update_city_coordinates,
    add_single_entity,
    update_entity_attribute,
    delete_entity_by_name,
)
from weather import get_weather
from geopy.geocoders import Nominatim
from db.seed import session




def test_db(user_name):
    print("Testing the Database")
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
        print(colored("5. Count the number of cities in a given state", "yellow"))
        print(colored("6. Exit", "yellow"))

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

            name = (
                input(colored(f"Enter {entity_type.__name__.lower()} name: ", "blue"))
                .strip()
                .lower()
            )
            add_single_entity(
                session,
                entity_type=entity_type,
                name=name.title(),
                population=0,
                area=0,
            )
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

            if entity_choice in entity_map:
                entity_type = entity_map[entity_choice]["type"]
                entity_name_input = (
                    input(
                        colored(
                            f"Enter the name of the {entity_map[entity_choice]['name']} to modify: ",
                            "blue",
                        )
                    )
                    .strip()
                    .lower()
                )
                attribute = (
                    input(colored("Enter the attribute to modify: ", "blue"))
                    .strip()
                    .lower()
                )
                new_value = (
                    input(colored("Enter the new value: ", "blue")).strip().lower()
                )

                update_entity_attribute(
                    session,
                    entity_type=entity_type,
                    entity_name=entity_name_input.title(),
                    attribute=attribute,
                    new_value=new_value,
                )
                display_entity(
                    session,
                    entity_type=entity_type,
                    entity_name=entity_name_input.title(),
                )
            else:
                print(colored("Invalid choice!", "red"))

        elif choice == "4":
            print(colored("\nChoose an entity to delete:", "red"))
            print(colored("a. State", "yellow"))
            print(colored("b. County", "yellow"))
            print(colored("c. City", "yellow"))

            sub_choice = input(colored("Enter your choice: ", "blue"))

            if sub_choice in entity_map:
                entity_name = input(
                    colored(
                        f"Enter {entity_map[sub_choice]['name']} name to delete: ",
                        "blue",
                    )
                ).strip()
                delete_entity_by_name(
                    session,
                    entity_name=entity_name.title(),
                    entity_cls=entity_map[sub_choice]["type"],
                )
                entity_map[sub_choice]["display"](session)
                
        elif choice == "5":
            state_name = input(colored("Enter city:  ", "blue"))
            count = session.query(func.count(City.id)).join(State).filter(State.name == state_name).scalar()
            print(colored(f"The number of cities in {state_name} is: {count}", "blue"))
                
                
        elif choice == "6":
            print(colored("Redirecting to the main Menu!", "magenta"))
            break
        else:
            ascii_banner = pyfiglet.figlet_format("Invalid choice. Please try again.")
            print(ascii_banner)