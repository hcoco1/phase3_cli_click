import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import click
from lib.db.models import State, County, City, Facilities, association_table as CityFacilityAssociation, Base
from lib.db.data import states_to_add, counties_to_add, cities_to_add, facilities_to_add, association_to_add
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, inspect
from faker import Faker
fake = Faker()

DATABASE_URL = "sqlite://///home/hcoco1/Development/code/phase-3/phase3_cli_click/lib/db/geodata.db"
engine = create_engine(DATABASE_URL)

# Use the Inspector to fetch the table names
# inspector = inspect(engine)
# print(inspector.get_table_names())
Session = sessionmaker(bind=engine)
session = Session()


@click.group()
def cli():
    """Manage the database records."""
    pass



@cli.command()
def create_tables():
    """Create all tables."""
    Base.metadata.create_all(engine)
    click.echo("✅ Done creating tables!")
    
    
@cli.command()
def seed_states():
    """Seed states."""
    session.query(State).delete()
    session.commit()
    session.add_all(states_to_add)
    session.commit()       
    click.echo("✅ Done seeding states!")

@cli.command()
def seed_counties():
    """Seed counties."""
    session.query(County).delete()
    session.commit()
    session.add_all(counties_to_add)
    session.commit()
    click.echo("✅ Done seeding counties!")

@cli.command()
def seed_cities():
    """Seed cities."""
    session.query(City).delete()
    session.commit()
    session.add_all(cities_to_add)
    session.commit()  
    click.echo("✅ Done seeding cities!")

@cli.command()
def seed_facilities():
    """Seed facilities."""
    session.query(Facilities).delete()
    session.commit()
    session.add_all(facilities_to_add)
    session.commit()
    click.echo("✅ Done seeding facilities!")
    
@cli.command()
def seed_associations():
    """Seed associations."""
    session.execute(CityFacilityAssociation.delete())  # Delete existing associations
    for association in association_to_add:
        session.execute(CityFacilityAssociation.insert().values(**association))
    session.commit()
    click.echo("✅ Done seeding associations!")

    
    

if __name__ == '__main__':
    print("🌱 Seeding DB...")
    cli()

# To create Tables: python seed.py create-tables
# To seed states: python seed.py seed-states
# To seed counties: python seed.py seed-counties
# To seed cities: python seed.py seed-cities
# To seed facilities: python seed.py seed-facilities
# To seed associations: python seed.py seed-associations





states_to_add = [
    State(
        name="Alabama",
        abbreviation="AL",
        population=4903185,
        capital="Montgomery",
        area=52420,
    ),
    State(
        name="Florida",
        abbreviation="FL",
        population=21538187,
        capital="Tallahassee",
        area=65758,
    ),
]


counties_to_add = [
    County(name="Miami-Dade", population=2763366, area=733, state_id=2),
    County(name="Broward", population=2003268, area=466, state_id=2),
    County(name="Palm Beach", population=1543809, area=760, state_id=2),
    County(name="Hillsborough", population=1528924, area=394, state_id=2),
    County(name="Jefferson", population=679599, area=429, state_id=1),
    County(name="Mobile", population=415355, area=474, state_id=1),
    County(name="Madison", population=404155, area=310, state_id=1),
    County(name="Baldwin", population=246617, area=614, state_id=1),
]





cities_to_add = [
    City(
        name="Miami",
        population=921122,
        area=244.33,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=2,
        county_id=1,
    ),
    City(
        name="Orlando",
        population=921122,
        area=244.33,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=2,
        county_id=1,
    ),
    City(
        name="Tampa",
        population=921122,
        area=244.33,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=2,
        county_id=1,
    ),
    City(
        name="Jacksonville",
        population=13191,
        area=367.63,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=2,
        county_id=2,
    ),
    City(
        name="Fort Lauderdale",
        population=13191,
        area=367.63,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=2,
        county_id=2,
    ),
    City(
        name="Tallahassee",
        population=13191,
        area=367.63,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=2,
        county_id=2,
    ),
    City(
        name="West Palm Beach",
        population=514603,
        area=253.33,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=2,
        county_id=3,
    ),
    City(
        name="Sarasota",
        population=514603,
        area=253.33,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=2,
        county_id=3,
    ),
    City(
        name="Daytona Beach",
        population=514603,
        area=253.33,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=2,
        county_id=3,
    ),
    City(
        name="St. Petersburg",
        population=509641,
        area=131.33,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=2,
        county_id=4,
    ),
    City(
        name="Naples",
        population=509641,
        area=131.33,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=2,
        county_id=4,
    ),
    City(
        name="Gainesville",
        population=509641,
        area=131.33,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=2,
        county_id=4,
    ),
    City(
        name="Birmingham",
        population=226533,
        area=143.00,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=1,
        county_id=5,
    ),
    City(
        name="Montgomery",
        population=226533,
        area=143.00,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=1,
        county_id=5,
    ),
    City(
        name="Mobile",
        population=226533,
        area=143.00,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=1,
        county_id=5,
    ),
    City(
        name="Huntsville",
        population=138451,
        area=158.00,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=1,
        county_id=6,
    ),
    City(
        name="Tuscaloosa",
        population=138451,
        area=158.00,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=1,
        county_id=6,
    ),
    City(
        name="Dothan",
        population=138451,
        area=158.00,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=1,
        county_id=6,
    ),
    City(
        name="Auburn",
        population=134718,
        area=103.33,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=1,
        county_id=7,
    ),
    City(
        name="Decatur",
        population=134718,
        area=103.33,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=1,
        county_id=7,
    ),
    City(
        name="Hoover",
        population=134718,
        area=103.33,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=1,
        county_id=7,
    ),
    City(
        name="Gadsden",
        population=82205,
        area=204.67,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=1,
        county_id=8,
    ),
    City(
        name="Florence",
        population=82205,
        area=204.67,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=1,
        county_id=8,
    ),
    City(
        name="Anniston",
        population=82205,
        area=204.67,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        state_id=1,
        county_id=8,
    ),
]


facilities_to_add = [
    Facilities(
        name="Public School",
        description="An educational institution for children aged 5-18",
        facility_type="Education",
    ),
    Facilities(
        name="Public Library",
        description="A facility where people can borrow books and access digital resources",
        facility_type="Education",
    ),
    Facilities(
        name="Public Hospital",
        description="A healthcare institution providing treatment with specialized medical and nursing staff",
        facility_type="Healthcare",
    ),
]

association_to_add = [
    {"city_id": 1, "facility_id": 1},
    {"city_id": 1, "facility_id": 2},
    {"city_id": 1, "facility_id": 3},
    {"city_id": 2, "facility_id": 1},
    {"city_id": 2, "facility_id": 2},
    {"city_id": 2, "facility_id": 3},
    {"city_id": 3, "facility_id": 1},
    {"city_id": 3, "facility_id": 2},
    {"city_id": 3, "facility_id": 3},
    {"city_id": 4, "facility_id": 1},
    {"city_id": 4, "facility_id": 2},
    {"city_id": 4, "facility_id": 3},
    {"city_id": 5, "facility_id": 1},
    {"city_id": 5, "facility_id": 2},
    {"city_id": 5, "facility_id": 3},
    {"city_id": 6, "facility_id": 1},
    {"city_id": 6, "facility_id": 2},
    {"city_id": 6, "facility_id": 3},
    {"city_id": 7, "facility_id": 1},
    {"city_id": 7, "facility_id": 2},
    {"city_id": 7, "facility_id": 3},
    {"city_id": 8, "facility_id": 1},
    {"city_id": 8, "facility_id": 2},
    {"city_id": 8, "facility_id": 3},
    {"city_id": 9, "facility_id": 1},
    {"city_id": 9, "facility_id": 2},
    {"city_id": 9, "facility_id": 3},
    {"city_id": 10, "facility_id": 1},
    {"city_id": 10, "facility_id": 2},
    {"city_id": 10, "facility_id": 3},
    {"city_id": 11, "facility_id": 1},
    {"city_id": 11, "facility_id": 2},
    {"city_id": 11, "facility_id": 3},
    {"city_id": 12, "facility_id": 1},
    {"city_id": 12, "facility_id": 2},
    {"city_id": 12, "facility_id": 3},
    {"city_id": 13, "facility_id": 1},
    {"city_id": 13, "facility_id": 2},
    {"city_id": 13, "facility_id": 3},
    {"city_id": 14, "facility_id": 1},
    {"city_id": 14, "facility_id": 2},
    {"city_id": 14, "facility_id": 3},
    {"city_id": 15, "facility_id": 1},
    {"city_id": 15, "facility_id": 2},
    {"city_id": 15, "facility_id": 3},
    {"city_id": 16, "facility_id": 1},
    {"city_id": 16, "facility_id": 2},
    {"city_id": 16, "facility_id": 3},
    {"city_id": 17, "facility_id": 1},
    {"city_id": 17, "facility_id": 2},
    {"city_id": 17, "facility_id": 3},
    {"city_id": 18, "facility_id": 1},
    {"city_id": 18, "facility_id": 2},
    {"city_id": 18, "facility_id": 3},
    {"city_id": 19, "facility_id": 1},
    {"city_id": 19, "facility_id": 2},
    {"city_id": 19, "facility_id": 3},
    {"city_id": 20, "facility_id": 1},
    {"city_id": 20, "facility_id": 2},
    {"city_id": 20, "facility_id": 3},
    {"city_id": 21, "facility_id": 1},
    {"city_id": 21, "facility_id": 2},
    {"city_id": 21, "facility_id": 3},
    {"city_id": 22, "facility_id": 1},
    {"city_id": 22, "facility_id": 2},
    {"city_id": 22, "facility_id": 3},
    {"city_id": 23, "facility_id": 1},
    {"city_id": 23, "facility_id": 2},
    {"city_id": 23, "facility_id": 3},
    {"city_id": 24, "facility_id": 1},
    {"city_id": 24, "facility_id": 2},
    {"city_id": 24, "facility_id": 3},
]


