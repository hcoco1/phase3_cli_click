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
    add_single_entity,
    update_entity_attribute,
    delete_entity_by_name,
)
from db.seed import session


def choose_entity():
    print(colored("\nChoose an entity:", "red"))
    print(colored("a. State", "yellow"))
    print(colored("b. City", "yellow"))
    print(colored("c. County", "yellow"))
    
    entity_choice = input(colored("Enter your choice (a/b/c): ", "blue")).lower()
    
    return entity_choice


def test_db(user_name):
    print("Managing the Database")

    while True:
        print(colored("\nChoose a CRUD operation:", "red"))
        print(colored("1. Show US entities", "yellow"))
        print(colored("2. Add a new US Entity (State/City/County)", "yellow"))
        print(colored("3. Update an US Entity (State/City/County)", "yellow"))
        print(colored("4. Delete an US Entity (State/City/County)", "yellow"))
        print(colored("5. Count the number of cities in a given state", "yellow"))
        print(colored("6. Main Menu", "yellow"))
        
        entity_map = {
            "a": {"type": State, "name": "state", "display": display_states},
            "b": {"type": City, "name": "city", "display": display_cities},
            "c": {"type": County, "name": "county", "display": display_counties},
        }

        choice = input(colored("Enter your choice: ", "red"))
        if choice == "1":
            display_states(session)
            display_counties(session)
            display_cities(session)
            display_facilities(session)

        elif choice == "2":
            entity_choice = choose_entity()
            
            if entity_choice in entity_map:
                entity_info = entity_map[entity_choice]
                entity_type = entity_info["type"]
                
                name = input(colored(f"Enter {entity_type.__name__.lower()} name: ", "blue")).strip().lower()
                
                # prompts for population and area
                add_single_entity(session, entity_type=entity_type, name=name.title(), population=0, area=0)
                
                display_entity(session, entity_type=entity_type, entity_name=name.title())



        elif choice == "3":
                entity_choice = choose_entity()

                if entity_choice in entity_map:
                    entity_info = entity_map[entity_choice]
                    entity_type = entity_info["type"]
                    
                    entity_name_input = input(colored(f"Enter the name of the {entity_info['name']} to modify: ", "blue")).strip()
                    attribute = input(colored("Enter the attribute to modify: ", "blue")).strip().lower()
                    new_value = input(colored("Enter the new value: ", "blue")).strip()
                    
                    update_entity_attribute(session, entity_type=entity_type, entity_name=entity_name_input.title(), attribute=attribute, new_value=new_value)
                    
                    display_entity(session, entity_type=entity_type, entity_name=entity_name_input.title())
                    entity_info["display"](session)

        elif choice == "4":
            entity_choice = choose_entity()

            if entity_choice in entity_map:
                entity_info = entity_map[entity_choice]
                entity_name = input(colored(f"Enter {entity_info['name']} name to delete: ", "blue")).strip()
                
                delete_entity_by_name(session, entity_name=entity_name.title(), entity_cls=entity_info["type"])
                entity_info["display"](session)

        elif choice == "5":
            state_name = input(colored("Enter state: ", "blue")).title()
            count = session.query(func.count(City.id)).join(State).filter(State.name == state_name).scalar()
            print(colored(f"The number of cities in {state_name} is: {count}", "blue"))

        elif choice == "6":
            print(colored("Redirecting to the main Menu!", "magenta"))
            break
        else:
            ascii_banner = pyfiglet.figlet_format("Invalid choice. Please try again.")
            print(ascii_banner)

        # At the end of the loop, close the session (consider if it's suitable for your use case)
        session.close()