import database_operations
import display
from database_operations import session
from models import State, City, County
import datetime
from termcolor import colored
import pyfiglet



    

def get_user_query():

        # Ask the user for their name
    user_name = input(colored("Please enter your name (or type 'exit' to quit): ", "blue"))
    ascii_banner = pyfiglet.figlet_format(f"Hello {user_name}!")
    print(ascii_banner)

    if user_name.lower() == "exit":
        ascii_banner = pyfiglet.figlet_format("Goodbye!!!")
        print(ascii_banner)
        return None  # Return None if the user wants to exit

    # Get the current date and time
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Open a text file in append mode and save the details
    with open("user_details.txt", "a") as file:
        file.write(f"{user_name}, {current_datetime}\n")

    print(colored(f"Your name was saved successfully in our local storage!", "red"))
        
    
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
            display.display_states(session)
            display.display_counties(session)
            display.display_cities(session)
            display.display_facilities(session)
            

        elif choice == "2":
            state_name = input(colored("Enter state name: ", "blue")).strip().lower()
            database_operations.add_single_state(session, state_name.title())

        elif choice == "3":
            state_name = input(colored("Enter the name of the state where the city is located: ", "blue")).strip().lower()
            county_name = input(colored("Enter the name of the county where the city is located: ", "blue")).strip().lower()
            name = input(colored("Enter city name: ", "blue")).strip().lower()
            database_operations.add_single_city(session, name.title(), state_name.title(), county_name.title() )
            database_operations.update_city_coordinates()

        elif choice == "4":
            state_name = input(colored("Enter the name of the state where the county is located: ", "blue")).strip().lower()
            name = input(colored("Enter county name: ", "blue")).strip().lower()
            database_operations.add_single_county(session,name.title(), state_name.title() )
            
        elif choice == "5":
            state_name = input(colored("Enter the name of the state to modify: ", "blue")).strip().lower()
            attribute = input(colored("Enter the attribute to modify: ", "blue")).strip().lower()
            new_value = input(colored("Enter the new value: ", "blue")).strip().lower()
            database_operations.update_state_attribute(state_name.title(), attribute, new_value)
            
        elif choice == "6":
            city_name = input(colored("Enter the name of the city to modify: ", "blue")).strip().lower()
            attribute = input(colored("Enter the attribute to modify: ", "blue")).strip().lower()
            new_value = input(colored("Enter the new value: ", "blue")).strip().lower()
            database_operations.update_city_attribute(city_name.title(), attribute, new_value)

        elif choice == "7":
            county_name = input(colored("Enter the name of the county to modify: ", "blue")).strip().lower()
            attribute = input(colored("Enter the attribute to modify: ", "blue")).strip().lower()
            new_value = input(colored("Enter the new value: ", "blue")).strip().lower()
            database_operations.update_county_attribute(county_name.title(), attribute, new_value)
            
        elif choice == "8":
            state_name = input(colored("Enter state name to delete: ", "blue")).strip().lower()
            database_operations.delete_state_by_name(session, state_name.title())
            
        elif choice == "9":
            county_name = input(colored("Enter county name to delete: ", "blue")).strip().lower()
            database_operations.delete_county_by_name(session, county_name.title())
            
        elif choice == "10":
            city_name = input(colored("Enter city name to delete: ", "blue")).strip().lower()
            database_operations.delete_city_by_name(session, city_name.title())

        elif choice == "11":
            ascii_banner = pyfiglet.figlet_format(f"Goodbye {user_name}!!!")
            print(ascii_banner)
            break

        else:
            ascii_banner = pyfiglet.figlet_format("Invalid choice. Please try again.")
            print(ascii_banner)
            






