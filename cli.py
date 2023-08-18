#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from models import State, County, City, Facilities
from user_interaction import start




if __name__ == "__main__":
    
    engine = create_engine('sqlite:///geodata.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(State).delete()
    session.query(County).delete()
    session.query(City).delete()
    session.query(Facilities).delete()

    try:
        
        start()
        

    except SQLAlchemyError as e:
        session.rollback()
        print(f"An error occurred: {e}")

    finally:
        session.close()
