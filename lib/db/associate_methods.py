import sys
sys.path.append('/home/hcoco1/Development/code/phase-3/phase3_cli_click')
import os
base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_path)
import click
from lib.db.models import State, County, City, Facilities, association_table
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

# Construct the absolute path to the database file
database_path = os.path.join(base_path, "geodata.db")
engine = create_engine(f"sqlite:///{database_path}")
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

# Associate Method 1: Adding a City to a State
@click.command()
@click.argument('city_name')
@click.argument('state_name')
def add_city_to_state(city_name, state_name):
    state = session.query(State).filter_by(name=state_name).first()
    if not state:
        click.echo(f"State {state_name} not found!")
        return
    
    new_city = City(name=city_name)
    state.cities.append(new_city)
    session.add(new_city)
    session.commit()
    click.echo(f"City {city_name} added to State {state_name}!")

# Associate Method 2: Linking a City to a Facility
@click.command()
@click.argument('city_name')
@click.argument('facility_name')
def link_city_to_facility(city_name, facility_name):
    city = session.query(City).filter_by(name=city_name).first()
    facility = session.query(Facilities).filter_by(name=facility_name).first()
    
    if not city or not facility:
        click.echo(f"City {city_name} or Facility {facility_name} not found!")
        return

    city.facilities.append(facility)
    session.commit()
    click.echo(f"Linked City {city_name} to Facility {facility_name}!")

# Associate Method 3: Moving a City to a Different County
@click.command()
@click.argument('city_name')
@click.argument('new_county_name')
def move_city_to_county(city_name, new_county_name):
    city = session.query(City).filter_by(name=city_name).first()
    new_county = session.query(County).filter_by(name=new_county_name).first()
    
    if not city or not new_county:
        click.echo(f"City {city_name} or County {new_county_name} not found!")
        return

    city.county = new_county
    session.commit()
    click.echo(f"Moved City {city_name} to County {new_county_name}!")

cli.add_command(add_city_to_state)
cli.add_command(link_city_to_facility)
cli.add_command(move_city_to_county)

if __name__ == '__main__':
    cli()
    
    
# python associate_methods.py add-city-to-state 'Pleasantville' 'Nevada'

"""
SELECT c.name AS City, s.name AS State
FROM Cities c
JOIN States s ON c.state_id = s.id
WHERE c.name = 'Pleasantville' AND s.name = 'Nevada';

"""

# python associate_methods.py link-city-to-facility 'Pleasantville' 'Ross LLC'

"""
    
SELECT c.name AS City, f.name AS Facility
FROM Cities c
JOIN CityFacilityAssociation cfa ON c.id = cfa.city_id
JOIN Facilities f ON cfa.facility_id = f.id;

SELECT c.name AS City, f.name AS Facility
FROM Cities c
JOIN CityFacilityAssociation cfa ON c.id = cfa.city_id
JOIN Facilities f ON cfa.facility_id = f.id
WHERE c.name = 'Pleasantville';


    """

# python associate_methods.py move-city-to-county 'Pleasantville' 'Susanside'
