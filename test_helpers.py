from lib.helpers import add_entities_general, Session
from lib.db.models import State, County, City, Facilities
from lib.db.data import facilities_to_add, counties_to_add, cities_to_add


add_entities_general(Facilities, facilities_to_add)
add_entities_general(County, counties_to_add)
add_entities_general(City, cities_to_add)




