import random
from sqlalchemy.orm import sessionmaker


from sqlalchemy import create_engine

DATABASE_URL = "sqlite://///home/hcoco1/Development/code/phase-3/phase3_cli_click/lib/db/geodata.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

from sqlalchemy.orm import sessionmaker
from lib.db.models import City, Facilities, association_table


# Create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Fetch all city IDs
city_ids = [city.id for city in session.query(City.id).all()]

# Fetch all facility IDs
facility_ids = [facility.id for facility in session.query(Facilities.id).all()]

# Define a list to store the associations
associations_to_add = []

# You can decide how many associations you want to create.
# For example, if you want to associate each city with 3 random facilities:
for city_id in city_ids:
    chosen_facilities = random.sample(facility_ids, 3)
    for facility_id in chosen_facilities:
        association = {"city_id": city_id, "facility_id": facility_id}
        associations_to_add.append(association)

# Add the associations to the session and commit
for association in associations_to_add:
    session.execute(association_table.insert().values(**association))

session.commit()

print("Associations populated successfully!")


