import click
from  db.models import State, County, City, Facilities, Base, association_table
from sqlalchemy.orm import sessionmaker
from db.data import states_to_add, counties_to_add, cities_to_add, facilities_to_add
from sqlalchemy import create_engine, inspect

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
    
    

if __name__ == '__main__':
    print("🌱 Seeding DB...")
    cli()

# To create Tables: python seed.py create-tables
# To seed states: python seed.py seed-states
# To seed counties: python seed.py seed-counties
# To seed cities: python seed.py seed-cities
# To seed facilities: python seed.py seed-facilities
# To seed associations: python seed.py seed-associations