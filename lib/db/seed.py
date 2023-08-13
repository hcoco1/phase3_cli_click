import click
from models import State, County, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
from geopy.geocoders import Nominatim
from geopy import exc
import time

fake = Faker()

@click.group()
def cli():
    pass

@cli.command()
@click.option("--num-states", default=50, help="Number of states to add")
@click.option("--num-counties", default=50, help="Number of counties to add")
@click.option("--num-cities", default=50, help="Number of cities to add")
def seed_db(num_states, num_counties, num_cities):
    print("🌱 Seeding DB...")

    engine = create_engine('sqlite:///geodata.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    delete_records(session)

    added_states = create_states(session, num_states)
    added_counties = create_counties(session, num_counties)
    added_cities = create_cities(session, num_cities)

    print("✅ Done seeding!")


def delete_records(session):
    session.query(State).delete()
    session.query(County).delete()
    session.query(City).delete()
    session.commit()


def create_states(session, num_states):
    states_to_add = []

    for _ in range(num_states):
        random_population = random.randint(1500, 50000)
        random_area = random.randint(500, 10000)
        state = State(
            name=fake.state(),
            abbreviation=fake.state_abbr(),
            population=random_population,
            capital=fake.city(),
            area=random_area,
        )
        states_to_add.append(state)
        session.add(state)

    if len(states_to_add) % 10 == 0:
        print(f"Committing {len(states_to_add)} states...")
        session.commit()  # Commit every 10 states

    session.commit()
    return states_to_add


def create_counties(session,num_counties):
    counties_to_add = []

    for _ in range(num_counties):
        random_population = random.randint(1500, 50000)
        random_area = random.randint(500, 10000)
        county = County(
            name=fake.city(), population=random_population, area=random_area
        )
        counties_to_add.append(county)
        session.add(county)

        if len(counties_to_add) % 10 == 0:
            session.commit()  # Commit every 10 states

    session.commit()
    return counties_to_add


def create_cities(session, num_cities):
    cities_to_add = []

    for _ in range(num_cities):
        random_population = random.randint(1500, 50000)
        random_area = random.randint(500, 10000)
        city = City(
            name=fake.city(),
            population=random_population,
            area=random_area,
            latitude=0,
            longitude=0,
            county_name=fake.city(),
        )
        cities_to_add.append(city)
        session.add(city)

        if len(cities_to_add) % 10 == 0:
            session.commit()  # Commit every 10 states

    session.commit()
    return cities_to_add

@cli.command()
def update_city_coordinates():
    engine = create_engine('sqlite:///geodata.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_agent_name = "GeoApp v1.0 (hcoco1@hotmail.com.com)"
    geolocator = Nominatim(user_agent=user_agent_name)
    
    # Fetch all cities with latitude and longitude values equal to 0
    cities_to_update = (
        session.query(City).filter((City.latitude == 0) & (City.longitude == 0)).all()
    )

    for city in cities_to_update:
        try:
            location = geolocator.geocode(f"{city.name}")
            if location:
                city.latitude = location.latitude
                city.longitude = location.longitude
                print(
                    f"Updated coordinates for {city.name}: {city.latitude}, {city.longitude}"
                )
                session.commit()
            time.sleep(1)  # Delay for 1 second between requests
        except exc.GeocoderServiceError:
            print(f"Service error when geocoding {city.name}. Skipping...")
            continue
        except exc.GeocoderUnavailable:
            print(f"Geocoding service unavailable for {city.name}. Skipping...")
            continue
        
    session.close()


if __name__ == '__main__':
     cli()
