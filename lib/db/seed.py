import sys
sys.path.append('/home/hcoco1/Development/code/phase-3/phase3_cli_click')
import os
base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_path)
import click
from lib.db.models import State, County, City, Facilities
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.data import states_to_add, counties_to_add, cities_to_add, facilities_to_add

# Get the absolute path of the script's directory
base_path = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the database file
database_path = os.path.join(base_path, "geodata.db")
engine = create_engine(f"sqlite:///{database_path}")
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    """Manage the database records."""
    pass

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

if __name__ == '__main__':
    cli()


# To seed states: python seed.py seed-states
# To seed counties: python seed.py seed-counties
# To seed cities: python seed.py seed-cities
# To seed facilities: python seed.py seed-facilities