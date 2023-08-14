#!/usr/bin/env python3
import sys
sys.path.append('/home/hcoco1/Development/code/phase-3/phase3_cli_click')
import os
base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_path)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Importing models and functions from other files
from lib.db.models import Base
from lib.db.seed import session
from  lib.user_interactions.user_interaction import start




if __name__ == "__main__":
    
    database_path = os.path.join(base_path, "geodata.db")
    engine = create_engine(f"sqlite:///{database_path}")    
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        
        start()
        

    except SQLAlchemyError as e:
        session.rollback()
        print(f"An error occurred: {e}")

    finally:
        session.close()
