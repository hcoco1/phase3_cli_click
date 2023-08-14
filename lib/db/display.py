import sys
sys.path.append('/home/hcoco1/Development/code/phase-3/phase3_cli_click')
import os
base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_path)
from prettytable.colortable import ColorTable, Themes, Theme
from lib.db.models import State, County, City, Facilities

# ALL STATES
def display_states(session):
    
    add_states = session.query(State).all()
    # Create a new table
    table = ColorTable(theme=Themes.OCEAN)
    table.align = "l"
    # Set the headers for your table columns
    table.field_names = ["ID", "Name", "Abbreviation", "Population", "Capital", "Area"]
    # Add rows to the table
    for state in add_states:
        # print(colored(state, "blue", "on_white"))
        table.add_row(
            [
                state.id,
                state.name,
                state.abbreviation,
                state.population,
                state.capital,
                state.area,
            ]
        )
    print("-" * len("STATE Table"))
    print("STATE Table")
    print("-" * len("STATE Table"))
    # Print the table
    print(table)


# ALL COUNTIES
def display_counties(session):
    add_counties = session.query(County).all()

    # Create a new theme instance based on the OCEAN theme and change only the font color
    custom_font_color_theme = Theme(
        default_color="93",  # Yellow for font color
        vertical_color=Themes.OCEAN.vertical_color,
        horizontal_color=Themes.OCEAN.horizontal_color,
        junction_color=Themes.OCEAN.junction_color,
    )

    # Create a new table with the custom font color theme
    table = ColorTable(theme=custom_font_color_theme)
    table.align = "l"
    # Set the headers for your table columns
    table.field_names = ["ID", "Name", "Population", "Area"]
    # Add rows to the table
    for county in add_counties:
        table.add_row(
            [county.id, county.name, county.population, county.area]
        )
    # Print the title
    print("-" * len("COUNTy Table"))
    print("COUNTIES Table")
    print("-" * len("COUNTy Table"))
    # Print the table
    print(table)


# ALL CITIES
def display_cities(session):
    add_cities = session.query(City).all()
    # Create a new theme instance based on the OCEAN theme and change only the font color
    custom_font_color_theme = Theme(
        default_color="50",  # Yellow for font color
        vertical_color=Themes.OCEAN.vertical_color,
        horizontal_color=Themes.OCEAN.horizontal_color,
        junction_color=Themes.OCEAN.junction_color,
    )
    # Create a new table with the custom font color theme
    table = ColorTable(theme=custom_font_color_theme)
    table.align = "l"
    # Set the headers for your table columns
    table.field_names = [
        "ID",
        "Name",
        "Population",
        "Area",
        "Latitude",
        "Longitude",
        "County Name",
    ]
    # Add rows to the table

    for city in add_cities:
        # print(colored(city, "yellow", "on_magenta"))
        table.add_row(
            [
                city.id,
                city.name,
                city.population,
                city.area,
                city.latitude,
                city.longitude,
                city.county_name,
                
            ]
        )
        # Print the title
    print("-" * len("CITY Table"))
    print("CITY Table")
    print("-" * len("CITY Table"))
    # Print the table
    print(table)


    session.close()
    
def display_facilities(session):
    add_facilities = session.query(Facilities).all()
    # Create a new theme instance based on the OCEAN theme and change only the font color
    custom_font_color_theme = Theme(
        default_color="50",  # Yellow for font color
        vertical_color=Themes.OCEAN.vertical_color,
        horizontal_color=Themes.OCEAN.horizontal_color,
        junction_color=Themes.OCEAN.junction_color,
    )
    # Create a new table with the custom font color theme
    table = ColorTable(theme=custom_font_color_theme)
    table.align = "l"
    # Set the headers for your table columns
    table.field_names = [
        "ID",
        "name",
        "Description",
        "Type"
    ]
    # Add rows to the table

    for facility in add_facilities:
        # print(colored(city, "yellow", "on_magenta"))
        table.add_row(
            [
                facility.id,
                facility.name,
                facility.description,
                facility.facility_type,
     
                
            ]
        )
        # Print the title
    print("-" * len("FACILITIES Table"))
    print("FACILITIES Table")
    print("-" * len("FACILITIES Table"))
    # Print the table
    print(table)


    session.close()