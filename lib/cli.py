#!/usr/bin/env python3
import sys
sys.path.append('/home/hcoco1/Development/code/phase-3/phase3_cli_click')
import os
base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_path)

from lib.helpers import Session, engine  # Import the centralized session factory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from helpers import (
    add_states,
    add_counties,
    add_cities,
    update_state_attribute, 
    update_county_attribute,
    update_city_attribute,
    delete_state_by_name,
    delete_county_by_name,
    delete_city_by_name,
    update_city_coordinates,
    session,
    add_single_state,
    add_single_county,
    add_single_city,
    add_facilities,
    populate_city_facility_association,
    print_city_facilities,
    Base
    
    
)
# from user_interaction import get_user_query
# from display import display_states, display_counties, display_cities
# from data import  values_list



if __name__ == "__main__":
    
    # Database setup
    engine = create_engine("sqlite:///lib/db/geodata.db")
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
   
  

    try:
        
        #get_user_query()
        
        # Add data to the database
        
        #add_states(session)
        # add_counties(session)
         #add_facilities(session)
        # populate_city_facility_association(values_list)
        # add_cities(session)
        # print_city_facilities(session)
        
        # add_single_state(session, "Alabama", population=4903185, area=52420.0)

        # add_single_county(session, "Georgia County", "Georgia", population=10, area=110)
        
        # add_single_city(session, "Atlanta", "Georgia", "Georgia County", population=210, area=2220, latitude=0, longitude=0)

        # update_city_coordinates()

        # update_state_attribute("Florida", "population", 9000000)
        # update_county_attribute("Orange", "population", 1650000)
        # update_city_attribute("Orlando", "population", 1350000)

        # delete_state_by_name(session, "Alabama")
        # delete_county_by_name(session, "Orange")
        # delete_city_by_name(session, "Orlando")

        # Display data using prettytable
        # display_states(session)
        # display_counties(session)
        # display_cities(session)

    except SQLAlchemyError as e:
        session.rollback()
        print(f"An error occurred: {e}")

    finally:
        session.close()
