import click

from models import State, County, City, Facilities, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data import states_to_add, counties_to_add, cities_to_add, facilities_to_add, generate_cities_for_states


engine = create_engine('sqlite:///geodata.db')
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
    cities = generate_cities_for_states(session)
    try:
        session.add_all(cities)
        session.commit()
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
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

# To create Tables: python seed.py create_tables
# To seed states: python seed.py seed-states
# To seed counties: python seed.py seed-counties
# To seed cities: python seed.py seed-cities
# To seed facilities: python seed.py seed-facilities