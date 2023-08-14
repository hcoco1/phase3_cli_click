import click
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from geodata_logic import (
    show_all_logic,
    add_state_logic,
    add_all_states_logic,
    add_all_counties_logic,
    add_all_cities_logic,
    add_city_logic,
    update_state_logic,
    add_county_logic,
    add_city_logic,
    update_state_logic,
    update_county_logic,
    update_city_logic,
    delete_state_logic,
    delete_county_logic,
    delete_city_logic,
    update_coordinates_logic,
    show_states_logic,
    show_counties_logic,
    show_cities_logic
)

import logging

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.ERROR)

Base = declarative_base()
engine = create_engine("sqlite:///geodata.db")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()



@click.group()
def cli():
    """GeoData Management Tool"""
    pass

@cli.command()
def show_all():
    """Display all states, counties, and cities in colored tables."""
    show_all_logic()

@cli.command()
def show_states():
    """Display all states in a colored Table."""
    show_states_logic()

@cli.command()
def show_counties():
    """Display all counties in a colored Table."""
    show_counties_logic()

@cli.command()
def show_cities():
    """Display all cities in a colored Table."""
    show_cities_logic()


@cli.command()
def add_all_states():
    """Add all states from predefined list."""
    add_all_states_logic()

@cli.command()
@click.option("--name", prompt="State Name")
@click.option("--population", type=int, default=0, prompt="Population")
@click.option("--area", type=float, default=0.0, prompt="Area")
def add_state(name, population, area):
    """Add a new state."""
    add_state_logic(name, population, area)

@cli.command()
@click.argument("state_name", required=True)
def add_all_counties(state_name):
    """Add counties for a given state from a predefined list."""
    add_all_counties_logic(state_name)

@cli.command()
@click.option("--name", prompt="County Name")
@click.argument("state_name", required=True)
@click.option("--population", type=int, default=0, prompt="Population")
@click.option("--area", type=float, default=0.0, prompt="Area")
def add_county(name, state_name, population, area):
    """Add a single county."""
    add_county_logic(name, state_name, population, area)

@cli.command()
@click.option("--name", prompt="City Name")
@click.argument("state_name", required=True)
@click.argument("county_name", required=True)
@click.option("--population", type=int, default=0, prompt="Population")
@click.option("--area", type=float, default=0.0, prompt="Area")
@click.option("--latitude", type=float, default=0.0, prompt="Latitude")
@click.option("--longitude", type=float, default=0.0, prompt="Longitude")
def add_city(name, state_name, county_name, population, area, latitude, longitude):
    """Add a single city."""
    add_city_logic(name, state_name, county_name, population, area, latitude, longitude)



@cli.command()
@click.argument("state_name", required=True)
@click.argument("attribute", required=True)
@click.argument("new_value", required=True)
def update_state(state_name, attribute, new_value):
    """Update attributes of a state."""
    update_state_logic(state_name, attribute, new_value)

@cli.command()
@click.argument("county_name", required=True)
@click.argument("attribute", required=True)
@click.argument("new_value", required=True)
def update_county(county_name, attribute, new_value):
    """Update attributes of a county."""
    update_county_logic(county_name, attribute, new_value)

@cli.command()
@click.argument("city_name", required=True)
@click.argument("attribute", required=True)
@click.argument("new_value", required=True)
def update_city(city_name, attribute, new_value):
    """Update attributes of a city."""
    update_city_logic(city_name, attribute, new_value)

@cli.command()
@click.argument("state_name", required=True)
def delete_state(state_name):
    """Delete a state by name."""
    delete_state_logic(state_name)

@cli.command()
@click.argument("county_name", required=True)
def delete_county(county_name):
    """Delete a county by name."""
    delete_county_logic(county_name)

@cli.command()
@click.argument("city_name", required=True)
def delete_city(city_name):
    """Delete a city by name."""
    delete_city_logic(city_name)

@cli.command("update-coordinates")
def update_coordinates():
    """Update coordinates for cities."""
    update_coordinates_logic()

if __name__ == "__main__":
    cli()
