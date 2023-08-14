from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
from termcolor import colored
from lib.db.models import State, County, City, Facilities
from geopy.geocoders import Nominatim
from geopy import exc
from lib.db.seed import Session, session
from sqlalchemy.exc import SQLAlchemyError
import time
import logging
user_agent_name = "GeoApp v1.0 (hcoco1@hotmail.com.com)"
geolocator = Nominatim(user_agent=user_agent_name)
logging.basicConfig(level=logging.DEBUG)


# General CRUD Functions




def add_single_state(session, name,  population=0, area=0):
    existing_state = session.query(State).filter_by(name=name).first()
    if existing_state:
        print(colored(f"State {name} already exists!", "yellow"))
        return

    try:
        new_state = State(name=name, population=population, area=area)
        session.add(new_state)
        session.commit()
        print(f"State {name} added successfully!")
    except SQLAlchemyError as e:
        session.rollback()
        print(colored(f"Error adding state {name}: {e} Try again!", "red"))
        
        
def add_single_city(session, name,  population=0, area=0):
    existing_city = session.query(City).filter_by(name=name).first()
    if existing_city:
        print(colored(f"City {name} already exists!", "yellow"))
        return

    try:
        new_city = City(name=name, population=population, area=area)
        session.add(new_city)
        session.commit()
        print(f"City {name} added successfully!")
    except SQLAlchemyError as e:
        session.rollback()
        print(colored(f"Error adding city {name}: {e} Try again!", "red"))
        
        
def add_single_county(session, name,  population=0, area=0):
        existing_county = session.query(County).filter_by(name=name).first()
        if existing_county:
            print(colored(f"County {name} already exists!", "yellow"))
            return

        try:
            new_county = County(name=name, population=population, area=area)
            session.add(new_county)
            session.commit()
            print(f"County {name} added successfully!")
        except SQLAlchemyError as e:
            session.rollback()
            print(colored(f"Error adding county {name}: {e} Try again!", "red"))
            
# UPDATE




def update_entity_attribute(session, entity_cls, entity_name, attribute, new_value):
    entity_to_update = session.query(entity_cls).filter_by(name=entity_name).first()

    if entity_to_update:
        print(colored("Before update:", getattr(entity_to_update, attribute), "yellow"))
        setattr(entity_to_update, attribute, new_value)
        session.commit()
        print(colored("After update:", getattr(entity_to_update, attribute), "green"))
    else:
        print(colored(f"{entity_cls.__name__} {entity_name} not found!", "red"))


# Usage example
# update_entity_attribute(session, State, "California", "population", 40000000)



# DELETE




def delete_entity_by_name(session, entity_cls, entity_name):
    try:
        print(f"Attempting to delete {entity_cls.__name__} {entity_name}...")
        entity = session.query(entity_cls).filter_by(name=entity_name).first()
        if entity:
            session.delete(entity)
            session.commit()
            print(colored(f"{entity_cls.__name__} {entity_name} deleted successfully!", "green"))
        else:
            print(f"{entity_cls.__name__} {entity_name} not found!")
    except SQLAlchemyError as e:
        session.rollback()
        print(colored(f"Error deleting {entity_cls.__name__} {entity_name}: {e}", "red"))
        print("Rollback executed due to exception.")

# Usage example
#delete_entity_by_name(session, State, "California")
#delete_entity_by_name(session, County, "Los Angeles County")
#delete_entity_by_name(session, City, "Los Angeles")


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


def add_entity(instance, model):
    """Add a single instance of a model to the database."""
    with Session() as session:
        try:
            # Check if the instance exists before adding.
            existing = session.query(model).filter_by(name=instance).first()
            if not existing:
                session.add(instance)
                session.commit()
                print(
                    colored(
                        f"{model.__name__} with ID {instance.id} added successfully!",
                        "green",
                    )
                )
            else:
                print(
                    colored(
                        f"{model.__name__} with ID {instance.id} already exists!",
                        "yellow",
                    )
                )
        except Exception as e:
            session.rollback()
            print(
                colored(
                    f"Error occurred while adding {model.__name__} with ID {instance.id}: {e}",
                    "red",
                )
            )

def add_entities_general(model, entities):
    with Session() as session:
        try:
            logging.debug(f"Adding entities: {entities}")
            session.add_all(entities)
            session.commit()
        except Exception as e:
            session.rollback()
            logging.error(f"Error occurred while adding entities: {e}")
            print(colored(f"Error occurred while adding entities: {e}", "red"))

def update_entity_general(model, filter_criteria, update_values):
    """Update attributes of an entity based on filter criteria."""
    with Session() as session:
        try:
            entities_to_update = session.query(model).filter_by(**filter_criteria).all()
            for entity in entities_to_update:
                for key, value in update_values.items():
                    setattr(entity, key, value)
            session.commit()
        except Exception as e:
            session.rollback()
            print(colored(f"Error occurred while updating entities: {e}", "red"))

def delete_entities_general(model, filter_criteria):
    """Delete entities of a given model based on filter criteria."""
    with Session() as session:
        try:
            entities_to_delete = session.query(model).filter_by(**filter_criteria).all()
            for entity in entities_to_delete:
                session.delete(entity)
            session.commit()
        except Exception as e:
            session.rollback()
            print(colored(f"Error occurred while deleting entities: {e}", "red"))

def populate_city_facility_association(values_list):
    """Populate the association table between cities and facilities."""
    sql = text(
        "INSERT INTO CityFacilityAssociation (city_id, facility_id) VALUES (:city_id, :facility_id)"
    )

    with Session() as session:
        try:
            # Use bulk insert mechanism for better performance
            session.execute(
                sql,
                [
                    {"city_id": city_id, "facility_id": facility_id}
                    for city_id, facility_id in values_list
                ],
            )
            session.commit()
        except Exception as e:
            session.rollback()
            print(
                colored(
                    f"Error occurred while populating CityFacilityAssociation: {e}",
                    "red",
                )
            )

def print_city_facilities(session):
    """Print facilities associated with each city."""

    # Query all cities
    cities = session.query(City).all()

    # Iterate through cities and print associated facilities
    for city in cities:
        facilities = city.facilities or []
        facilities_names = [facility.name for facility in facilities]

        print(f"City: {city.name}")
        print(
            "Facilities:",
            ", ".join(facilities_names) or "No facilities associated with this city.",
        )
        print("=" * 30)

def update_city_coordinates():
    """Update city coordinates using the geolocation service."""
    with Session() as session:
        # Fetch all cities with latitude and longitude values equal to 0
        cities_to_update = (
            session.query(City)
            .filter((City.latitude == 0) & (City.longitude == 0))
            .all()
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
                else:
                    print(f"No coordinates found for {city.name}. Skipping...")
                time.sleep(1)  # Delay for 1 second between successful requests
            except exc.GeocoderServiceError:
                print(f"Service error when geocoding {city.name}. Skipping...")
            except exc.GeocoderUnavailable:
                print(f"Geocoding service unavailable for {city.name}. Skipping...")
            except Exception as e:
                print(
                    colored(
                        f"Unexpected error for {city.name}: {e}. Skipping...", "red"
                    )
                )

        # Commit all changes after updating all cities
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            print(colored(f"Error occurred while committing changes: {e}", "red"))
