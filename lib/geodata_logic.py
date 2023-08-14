import click
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from cli_display import display_states, display_counties, display_cities

from cli_database_operations import (
    add_states,
    add_counties,
    add_cities,
    update_state_attribute,
    update_county_attribute,
    update_city_attribute,
    delete_state_by_name,
    delete_county_by_name,
    delete_city_by_name,
    update_city_coordinates,
    session,
    add_single_state,
    add_single_county,
    add_single_city,
)


def show_all_logic():
    display_states(session)
    display_counties(session)
    display_cities(session)


def add_all_states_logic():
    return add_states(session)


def add_state_logic(name, population, area):
    return add_single_state(session, name, population, area)


def add_all_counties_logic(state_name):
    return add_counties(session, state_name)


def add_county_logic(name, state_name, population, area):
    return add_single_county(session, name, state_name, population, area)


def add_all_cities_logic():
    return add_cities(session)


def add_city_logic(
    name, state_name, county_name, population, area, latitude, longitude
):
    return add_single_city(
        session, name, state_name, county_name, population, area, latitude, longitude
    )


def update_state_logic(state_name, attribute, new_value):
    return update_state_attribute(state_name, attribute, new_value)


def update_county_logic(county_name, attribute, new_value):
    return update_county_attribute(county_name, attribute, new_value)


def update_city_logic(city_name, attribute, new_value):
    return update_city_attribute(city_name, attribute, new_value)


def delete_state_logic(state_name):
    return delete_state_by_name(session, state_name)


def delete_county_logic(county_name):
    return delete_county_by_name(session, county_name)


def delete_city_logic(city_name):
    return delete_city_by_name(session, city_name)


def update_coordinates_logic():
    update_city_coordinates()


def show_states_logic():
    display_states(session)


def show_counties_logic():
    display_counties(session)


def show_cities_logic():
    display_cities(session)
