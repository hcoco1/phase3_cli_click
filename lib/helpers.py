import sys
import time
import logging
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
from termcolor import colored
from db.models import State, County, City, Facilities
from geopy.geocoders import Nominatim
from geopy import exc
from db.seed import Session, session
from sqlalchemy.exc import SQLAlchemyError
logging.basicConfig(level=logging.INFO)


user_agent_name = "GeoApp v1.0 (hcoco1@hotmail.com.com)"
geolocator = Nominatim(user_agent=user_agent_name)
logging.getLogger("geopy").setLevel(logging.INFO)
logging.getLogger("urllib3").setLevel(logging.INFO)

# General CRUD Functions

def add_single_entity(session, entity_type, name, population=0, area=0):
    existing_entity = session.query(entity_type).filter_by(name=name).first()
    if existing_entity:
        print(colored(f"{entity_type.__name__} {name} already exists!", "yellow"))
        return

    try:
        new_entity = entity_type(name=name, population=population, area=area)
        session.add(new_entity)
        session.commit()
        print(f"{entity_type.__name__} {name} added successfully!")
    except SQLAlchemyError as e:
        session.rollback()
        print(
            colored(
                f"Error adding {entity_type.__name__.lower()} {name}: {e} Try again!",
                "red",
            )
        )


# add_single_entity(session, State, "California", 40000000, 423967)
# add_single_entity(session, City, "Los Angeles", 4000000, 503)
# add_single_entity(session, County, "Los Angeles County", 10000000, 4750)

def update_entity_attribute(session, entity_type, entity_name, attribute, new_value):
    # Convert space-separated attribute names to snake_case
    attribute_snake_case = attribute.replace(" ", "_").lower()

    # Fetch the entity
    entity_to_update = session.query(entity_type).filter_by(name=entity_name).first()

    if not entity_to_update:
        print(colored(f"{entity_type.__name__} named '{entity_name}' not found!", "red"))
        return

    # Check if the entity has the attribute
    if not hasattr(entity_to_update, attribute_snake_case):
        print(colored(f"{entity_type.__name__} does not have an attribute named '{attribute}'", "red"))
        return

    # Display the old value
    print(colored(f"Before update: {getattr(entity_to_update, attribute_snake_case)}", "yellow"))


    # Update the attribute with the new value
    setattr(entity_to_update, attribute_snake_case, new_value)
    session.commit()

    # Display the updated value
    print(colored(f"After update: {getattr(entity_to_update, attribute_snake_case)}", "green"))

# DELETE
def delete_entity_by_name(session, entity_cls, entity_name):
    try:
        print(f"Attempting to delete {entity_cls.__name__} {entity_name}...")
        entity = session.query(entity_cls).filter_by(name=entity_name).first()
        if entity:
            session.delete(entity)
            session.commit()
            print(
                colored(
                    f"{entity_cls.__name__} {entity_name} deleted successfully!",
                    "green",
                )
            )
        else:
            print(f"{entity_cls.__name__} {entity_name} not found!")
    except SQLAlchemyError as e:
        session.rollback()
        print(
            colored(f"Error deleting {entity_cls.__name__} {entity_name}: {e}", "red")
        )
        print("Rollback executed due to exception.")


# Usage example
# delete_entity_by_name(session, State, "California")
# delete_entity_by_name(session, County, "Los Angeles County")
# delete_entity_by_name(session, City, "Los Angeles")


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





def update_city_coordinates(city_name=None):
    """Update city coordinates using the geolocation service. If city_name is provided, updates only for that city."""
    with Session() as session:
        # Filter criteria for latitude and longitude values equal to 0 or None
        filter_criteria = (
            ((City.latitude == 0) | (City.latitude == None)) &
            ((City.longitude == 0) | (City.longitude == None))
        )

        # If a city_name is provided, add it to the filter criteria
        if city_name:
            filter_criteria &= (City.name == city_name)

        # Fetch cities based on filter criteria
        cities_to_update = session.query(City).filter(filter_criteria).all()

        for city in cities_to_update:
            try:
                location = geolocator.geocode(f"{city.name}")
                if location:
                    city.latitude = location.latitude
                    city.longitude = location.longitude
                    session.add(city)  # Ensure changes are staged for commit
                time.sleep(1)  # Delay for 1 second between successful requests
            except exc.GeocoderServiceError:
                pass
            except exc.GeocoderUnavailable:
                pass
            except Exception as e:
                pass

        # Commit all changes after updating cities
        try:
            session.commit()
        except Exception as e:
            session.rollback()



def print_animated_text(text, delay=0.1):
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)