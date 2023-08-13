from models import State, County, City, Facilities
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random



print("🌱 Seeding DB...")
engine = create_engine('sqlite:///geodata.db')

Session = sessionmaker(bind=engine)
session = Session()


def delete_records():
    session.query(State).delete()
    session.query(County).delete()
    session.query(City).delete()
    session.query(Facilities).delete()
    session.commit()
 
    

    
def create_states(num_states):
    fake = Faker()
    states_to_add = []

    for _ in range(num_states):
        random_population = random.randint(1500, 50000)
        random_area = random.randint(500, 10000)
        state = State(
            name=fake.state(),
            abbreviation=fake.state_abbr(),
            population=random_population,
            capital=fake.city(),
            area=random_area
        )
        states_to_add.append(state)

    session.add_all(states_to_add)
    session.commit()
    return states_to_add

def create_counties(num_counties):
    fake = Faker()
    counties_to_add = []

    for _ in range(num_counties):
        random_population = random.randint(1500, 50000)
        random_area = random.randint(500, 10000)
        county = County(
            name=fake.city(),
            population=random_population,
            area=random_area
        )
        counties_to_add.append(county)

    session.add_all(counties_to_add)
    session.commit()
    return counties_to_add









if __name__ == '__main__':
    delete_records()
    
    num_states_to_add = 51  # Specify the number of states you want to add
    added_states = create_states(num_states_to_add)
    
    num_counties_to_add = 50  # Specify the number of counties you want to add
    added_counties = create_counties(num_counties_to_add)
    

    print("✅ Done seeding!")

print("✅ Done seeding!")


