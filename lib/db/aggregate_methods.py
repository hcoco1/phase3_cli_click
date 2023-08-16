import sys
import os
from lib.db.models import State, County, City, Facilities, association_table
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
sys.path.append('/home/hcoco1/Development/code/phase-3/phase3_cli_click')
base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_path)


# Construct the absolute path to the database file

database_path = os.path.join(base_path, "geodata.db")
engine = create_engine(f"sqlite:///{database_path}")
Session = sessionmaker(bind=engine)
session = Session()

# Aggregate Method 1: Count the number of cities in a given state.
def count_cities_in_state(state_name):
    return session.query(func.count(City.id)).join(State).filter(State.name == state_name).scalar()

# Aggregate Method 2: Calculate the average population of cities in a given state.
def average_city_population_in_state(state_name):
    return session.query(func.avg(City.population)).join(State).filter(State.name == state_name).scalar()

# Aggregate Method 3: Find the total area of all cities in a given county.
def total_area_in_county(county_name):
    return session.query(func.sum(City.area)).join(County).filter(County.name == county_name).scalar()

# Aggregate Method 4: Count the number of facilities in a given city.
def count_facilities_in_city(city_name):
    return session.query(func.count(Facilities.id)).join(association_table).join(City).filter(City.name == city_name).scalar()

# Example Usage:
state_name = "California"
print(f"Number of cities in {state_name}: {count_cities_in_state(state_name)}")
print(f"Average population of cities in {state_name}: {average_city_population_in_state(state_name):.2f}")

county_name = "Alameda"
print(f"Total area of cities in {county_name} county: {total_area_in_county(county_name)}")

city_name = "San Francisco"
print(f"Number of facilities in {city_name}: {count_facilities_in_city(city_name)}")

session.close()
