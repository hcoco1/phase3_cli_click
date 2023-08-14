import sys
sys.path.append('/home/hcoco1/Development/code/phase-3/phase3_cli_click')
import os
base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_path)

import os
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

@click.command()
def seed_records():
    """Delete existing records and then seed the database with new records."""
    
    # Delete existing records
    session.query(State).delete()
    session.query(County).delete()
    session.query(City).delete()
    session.query(Facilities).delete()
    session.commit()
    click.echo("🗑️ Existing records deleted!")

    # Create new records
    session.add_all(states_to_add)
    session.add_all(counties_to_add)
    session.add_all(cities_to_add)
    session.add_all(facilities_to_add)
    session.commit()
    click.echo("✅ Done seeding!")

if __name__ == '__main__':
    seed_records()



# To seed: python seed_all_data.py