from lib.db.models import State, County, City, Facilities
from faker import Faker
import random
fake = Faker()

# fake states. Only to feed the tables. Not for plying Capital Game
states_to_add1=  [
    State(
        name= fake.city(),
        abbreviation = fake.state_abbr(),
        population = random.randint(1500, 50000),
        capital = fake.city(),
        area = random.randint(500, 10000),

        
    )
    for _ in range(52)  # Number of states
]



counties_to_add = [
    County(
        name= fake.city(),
        population= random.randint(1500, 50000),
        area= random.randint(500, 10000),
    )
    for _ in range(20)  # Number of states
]

cities_to_add = [
    City(
        name= fake.city(),
        population = random.randint(1500, 50000),
        area = random.randint(500, 10000),
        latitude = fake.coordinate(),
        longitude = fake.coordinate(),
        county_name = fake.city()
    )
    for _ in range(20)  # Number of states
]

# List of different facility types
facility_types = ["Education", "Healthcare", "Recreation", "Safety and Security", "Government", "Communication"]

facilities_to_add = [
    Facilities(
        name=fake.company(),
        description=fake.sentence(),
        facility_type=facility_types[i % len(facility_types)],
    )
    for i in range(11)  # Number of facilities
]

# List of real states REAL DATA FROM 2019 CENSUS    

states_to_add = [
    State(
        name="Alabama",
        abbreviation="AL",
        population=4903185,
        capital="Montgomery",
        area=52420,
    ),
    State(
        name="Alaska",
        abbreviation="AK",
        population=731545,
        capital="Juneau",
        area=665384,
    ),
    State(
        name="Arizona",
        abbreviation="AZ",
        population=7278717,
        capital="Phoenix",
        area=113990,
    ),
    State(
        name="Arkansas",
        abbreviation="AR",
        population=3017804,
        capital="Little Rock",
        area=53179,
    ),
    State(
        name="California",
        abbreviation="CA",
        population=39538223,
        capital="Sacramento",
        area=163695,
    ),
    State(
        name="Colorado",
        abbreviation="CO",
        population=5773714,
        capital="Denver",
        area=104094,
    ),
    State(
        name="Connecticut",
        abbreviation="CT",
        population=3565287,
        capital="Hartford",
        area=5543,
    ),
    State(
        name="Delaware",
        abbreviation="DE",
        population=973764,
        capital="Dover",
        area=2489,
    ),
    State(
        name="Florida",
        abbreviation="FL",
        population=21538187,
        capital="Tallahassee",
        area=65758,
    ),
    State(
        name="Georgia",
        abbreviation="GA",
        population=10617423,
        capital="Atlanta",
        area=59425,
    ),
    State(
        name="Hawaii",
        abbreviation="HI",
        population=1455271,
        capital="Honolulu",
        area=10932,
    ),
    State(
        name="Idaho",
        abbreviation="ID",
        population=1787065,
        capital="Boise",
        area=83569
    ),
    State(
        name="Illinois",
        abbreviation="IL",
        population=12671821,
        capital="Springfield",
        area=57914,
    ),
    State(
        name="Indiana",
        abbreviation="IN",
        population=6732219,
        capital="Indianapolis",
        area=36420,
    ),
    State(
        name="Iowa",
        abbreviation="IA",
        population=3155070,
        capital="Des Moines",
        area=56273,
    ),
    State(
        name="Kansas",
        abbreviation="KS",
        population=2913314,
        capital="Topeka",
        area=82278,
    ),
    State(
        name="Kentucky",
        abbreviation="KY",
        population=4467673,
        capital="Frankfort",
        area=40408,
    ),
    State(
        name="Louisiana",
        abbreviation="LA",
        population=4648794,
        capital="Baton Rouge",
        area=52378,
    ),
    State(
        name="Maine",
        abbreviation="ME",
        population=1344212,
        capital="Augusta",
        area=35380,
    ),
    State(
        name="Maryland",
        abbreviation="MD",
        population=6045680,
        capital="Annapolis",
        area=12406,
    ),
    State(
        name="Massachusetts",
        abbreviation="MA",
        population=6892503,
        capital="Boston",
        area=10554,
    ),
    State(
        name="Michigan",
        abbreviation="MI",
        population=9986857,
        capital="Lansing",
        area=96714,
    ),
    State(
        name="Minnesota",
        abbreviation="MN",
        population=5639632,
        capital="Saint Paul",
        area=86936,
    ),
    State(
        name="Mississippi",
        abbreviation="MS",
        population=2976149,
        capital="Jackson",
        area=48432,
    ),
    State(
        name="Missouri",
        abbreviation="MO",
        population=6137428,
        capital="Jefferson City",
        area=69707,
    ),
    State(
        name="Montana",
        abbreviation="MT",
        population=1068778,
        capital="Helena",
        area=147040,
    ),
    State(
        name="Nebraska",
        abbreviation="NE",
        population=1934408,
        capital="Lincoln",
        area=77348,
    ),
    State(
        name="Nevada",
        abbreviation="NV",
        population=3080156,
        capital="Carson City",
        area=110572,
    ),
    State(
        name="New Hampshire",
        abbreviation="NH",
        population=1359711,
        capital="Concord",
        area=9349,
    ),
    State(
        name="New Jersey",
        abbreviation="NJ",
        population=8882190,
        capital="Trenton",
        area=8723,
    ),
    State(
        name="New Mexico",
        abbreviation="NM",
        population=2117522,
        capital="Santa Fe",
        area=121590,
    ),
    State(
        name="New York",
        abbreviation="NY",
        population=19453561,
        capital="Albany",
        area=54555,
    ),
    State(
        name="North Carolina",
        abbreviation="NC",
        population=10488084,
        capital="Raleigh",
        area=53819,
    ),
    State(
        name="North Dakota",
        abbreviation="ND",
        population=762062,
        capital="Bismarck",
        area=70698,
    ),
    State(
        name="Ohio",
        abbreviation="OH",
        population=11689100,
        capital="Columbus",
        area=44826,
    ),
    State(
        name="Oklahoma",
        abbreviation="OK",
        population=3956971,
        capital="Oklahoma City",
        area=69903,
    ),
    State(
        name="Oregon",
        abbreviation="OR",
        population=4217737,
        capital="Salem",
        area=98379,
    ),
    State(
        name="Pennsylvania",
        abbreviation="PA",
        population=12801989,
        capital="Harrisburg",
        area=46054,
    ),
    State(
        name="Rhode Island",
        abbreviation="RI",
        population=1059361,
        capital="Providence",
        area=1545,
    ),
    State(
        name="South Carolina",
        abbreviation="SC",
        population=5148714,
        capital="Columbia",
        area=32020,
    ),
    State(
        name="South Dakota",
        abbreviation="SD",
        population=884659,
        capital="Pierre",
        area=77116,
    ),
    State(
        name="Tennessee",
        abbreviation="TN",
        population=6829174,
        capital="Nashville",
        area=42144,
    ),
    State(
        name="Texas",
        abbreviation="TX",
        population=28995881,
        capital="Austin",
        area=268596,
    ),
    State(
        name="Utah",
        abbreviation="UT",
        population=3271616,
        capital="Salt Lake City",
        area=84897,
    ),
    State(
        name="Vermont",
        abbreviation="VT",
        population=623989,
        capital="Montpelier",
        area=9616,
    ),
    State(
        name="Virginia",
        abbreviation="VA",
        population=8535519,
        capital="Richmond",
        area=42775,
    ),
    State(
        name="Washington",
        abbreviation="WA",
        population=7614893,
        capital="Olympia",
        area=71298,
    ),
    State(
        name="West Virginia",
        abbreviation="WV",
        population=1792147,
        capital="Charleston",
        area=24230,
    ),
    State(
        name="Wisconsin",
        abbreviation="WI",
        population=5822434,
        capital="Madison",
        area=65496,
    ),
    State(
        name="Wyoming",
        abbreviation="WY",
        population=578759,
        capital="Cheyenne",
        area=97813,
    ),
]


cities = [
    {
        "name": "Montgomery",
        "population": 198525,
        "area": 159.8,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Alabama",
        "county_name": 1846,
    },
    {
        "name": "Juneau",
        "population": 32113,
        "area": 2716.7,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Alaska",
        "county_name": 1906,
    },
    {
        "name": "Phoenix",
        "population": 1680992,
        "area": 517.6,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Arizona",
        "county_name": 1912,
    },
    {
        "name": "Little Rock",
        "population": 197312,
        "area": 116.2,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Arkansas",
        "county_name": 1821,
    },
    {
        "name": "Sacramento",
        "population": 513624,
        "area": 97.9,
        "latitude": 0,
        "longitude": 0,
        "state_name": "California",
        "county_name": 1854,
    },
    {
        "name": "Denver",
        "population": 727211,
        "area": 153.3,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Colorado",
        "county_name": 1867,
    },
    {
        "name": "Hartford",
        "population": 122105,
        "area": 17.3,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Connecticut",
        "county_name": 1875,
    },
    {
        "name": "Dover",
        "population": 38079,
        "area": 22.4,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Delaware",
        "county_name": 1777,
    },
    {
        "name": "Tallahassee",
        "population": 194500,
        "area": 95.7,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Florida",
        "county_name": 1824,
    },
    {
        "name": "Atlanta",
        "population": 506811,
        "area": 133.5,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Georgia",
        "county_name": 1868,
    },
    {
        "name": "Honolulu",
        "population": 345064,
        "area": 68.4,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Hawaii",
        "county_name": 1845,
    },
    {
        "name": "Boise",
        "population": 228959,
        "area": 63.8,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Idaho",
        "county_name": 1865,
    },
    {
        "name": "Springfield",
        "population": 114230,
        "area": 54,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Illinois",
        "county_name": 1837,
    },
    {
        "name": "Indianapolis",
        "population": 876384,
        "area": 361.5,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Indiana",
        "county_name": 1825,
    },
    {
        "name": "Des Moines",
        "population": 214237,
        "area": 75.8,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Iowa",
        "county_name": 1857,
    },
    {
        "name": "Topeka",
        "population": 125310,
        "area": 56,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Kansas",
        "county_name": 1856,
    },
    {
        "name": "Frankfort",
        "population": 27679,
        "area": 14.7,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Kentucky",
        "county_name": 1792,
    },
    {
        "name": "Baton Rouge",
        "population": 220236,
        "area": 76.8,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Louisiana",
        "county_name": 1880,
    },
    {
        "name": "Augusta",
        "population": 18681,
        "area": 55.4,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Maine",
        "county_name": 1832,
    },
    {
        "name": "Annapolis",
        "population": 39174,
        "area": 6.73,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Maryland",
        "county_name": 1694,
    },
    {
        "name": "Boston",
        "population": 692600,
        "area": 89.6,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Massachusetts",
        "county_name": 1630,
    },
    {
        "name": "Lansing",
        "population": 118210,
        "area": 35,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Michigan",
        "county_name": 1847,
    },
    {
        "name": "Saint Paul",
        "population": 308096,
        "area": 52.8,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Minnesota",
        "county_name": 1849,
    },
    {
        "name": "Jackson",
        "population": 160628,
        "area": 104.9,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Mississippi",
        "county_name": 1821,
    },
    {
        "name": "Jefferson City",
        "population": 42838,
        "area": 27.3,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Missouri",
        "county_name": 1826,
    },
    {
        "name": "Helena",
        "population": 3215,
        "area": 14,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Montana",
        "county_name": 1875,
    },
    {
        "name": "Lincoln",
        "population": 289102,
        "area": 74.6,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Nebraska",
        "county_name": 1867,
    },
    {
        "name": "Carson City",
        "population": 55916,
        "area": 143.4,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Nevada",
        "county_name": 1861,
    },
    {
        "name": "Concord",
        "population": 43627,
        "area": 64.3,
        "latitude": 0,
        "longitude": 0,
        "state_name": "New Hampshire",
        "county_name": 1808,
    },
    {
        "name": "Trenton",
        "population": 83203,
        "area": 7.66,
        "latitude": 0,
        "longitude": 0,
        "state_name": "New Jersey",
        "county_name": 1784,
    },
    {
        "name": "Santa Fe",
        "population": 84683,
        "area": 37.3,
        "latitude": 0,
        "longitude": 0,
        "state_name": "New Mexico",
        "county_name": 1610,
    },
    {
        "name": "Albany",
        "population": 96460,
        "area": 21.4,
        "latitude": 0,
        "longitude": 0,
        "state_name": "New York",
        "county_name": 1797,
    },
    {
        "name": "Raleigh",
        "population": 474069,
        "area": 114.6,
        "latitude": 0,
        "longitude": 0,
        "state_name": "North Carolina",
        "county_name": 1792,
    },
    {
        "name": "Bismarck",
        "population": 73529,
        "area": 26.9,
        "latitude": 0,
        "longitude": 0,
        "state_name": "North Dakota",
        "county_name": 1883,
    },
    {
        "name": "Columbus",
        "population": 898553,
        "area": 210.3,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Ohio",
        "county_name": 1816,
    },
    {
        "name": "Oklahoma City",
        "population": 655057,
        "area": 620.3,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Oklahoma",
        "county_name": 1910,
    },
    {
        "name": "Salem",
        "population": 174365,
        "area": 45.7,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Oregon",
        "county_name": 1855,
    },
    {
        "name": "Harrisburg",
        "population": 49528,
        "area": 8.11,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Pennsylvania",
        "county_name": 1812,
    },
    {
        "name": "Providence",
        "population": 179883,
        "area": 18.5,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Rhode Island",
        "county_name": 1900,
    },
    {
        "name": "Columbia",
        "population": 131674,
        "area": 125.2,
        "latitude": 0,
        "longitude": 0,
        "state_name": "South Carolina",
        "county_name": 1786,
    },
    {
        "name": "Pierre",
        "population": 13646,
        "area": 13,
        "latitude": 0,
        "longitude": 0,
        "state_name": "South Dakota",
        "county_name": 1889,
    },
    {
        "name": "Nashville",
        "population": 670820,
        "area": 525.9,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Tennessee",
        "county_name": 1826,
    },
    {
        "name": "Austin",
        "population": 978908,
        "area": 305.1,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Texas",
        "county_name": 1839,
    },
    {
        "name": "Salt Lake City",
        "population": 200567,
        "area": 109.1,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Utah",
        "county_name": 1858,
    },
    {
        "name": "Montpelier",
        "population": 7855,
        "area": 10.2,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Vermont",
        "county_name": 1805,
    },
    {
        "name": "Richmond",
        "population": 230436,
        "area": 60.1,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Virginia",
        "county_name": 1780,
    },
    {
        "name": "Olympia",
        "population": 46478,
        "area": 16.7,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Washington",
        "county_name": 1853,
    },
    {
        "name": "Charleston",
        "population": 46536,
        "area": 31.6,
        "latitude": 0,
        "longitude": 0,
        "state_name": "West Virginia",
        "county_name": 1885,
    },
    {
        "name": "Madison",
        "population": 259680,
        "area": 68.7,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Wisconsin",
        "county_name": 1838,
    },
    {
        "name": "Cheyenne",
        "population": 64235,
        "area": 21.1,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Wyoming",
        "county_name": 1869,
    },
]

cities_to_add1 = [
    City(
        name="Montgomery",
        population=198525,
        area=159.8,
        latitude=0,
        longitude=0,
        county_name="Montgomery",
    ),
    City(
        name="Juneau",
        population=32113,
        area=2716.7,
        latitude=0,
        longitude=0,
        county_name="Juneau",
    ),
    City(
        name="Phoenix",
        population=1680992,
        area=517.6,
        latitude=0,
        longitude=0,
        county_name="Maricopa",
    ),
    City(
        name="Little Rock",
        population=197312,
        area=116.2,
        latitude=0,
        longitude=0,
        county_name="Pulaski",
    ),
    City(
        name="Sacramento",
        population=513624,
        area=97.9,
        latitude=0,
        longitude=0,
        county_name="Sacramento",
    ),
    City(
        name="Denver",
        population=727211,
        area=153.3,
        latitude=0,
        longitude=0,
        county_name="Denver",
    ),
    City(
        name="Hartford",
        population=122105,
        area=17.3,
        latitude=0,
        longitude=0,
        county_name="Hartford",
    ),
    City(
        name="Dover",
        population=38079,
        area=22.4,
        latitude=0,
        longitude=0,
        county_name="Kent",
    ),
    City(
        name="Tallahassee",
        population=194500,
        area=95.7,
        latitude=0,
        longitude=0,
        county_name="Leon",
    ),
]


facilities_to_add1 = [
    Facilities(
        name="Public School",
        description="An educational institution for children aged 5-18",
        facility_type="Education",
    ),
    Facilities(
        name="Public Library",
        description="A facility where people can borrow books and access digital resources",
        facility_type="Education",
    ),
    Facilities(
        name="Public Hospital",
        description="A healthcare institution providing treatment with specialized medical and nursing staff",
        facility_type="Healthcare",
    ),
    Facilities(
        name="Community Park",
        description="A green area reserved for recreational activities, often equipped with playgrounds, benches, and sports fields",
        facility_type="Recreation",
    ),
    Facilities(
        name="Police Station",
        description="A building where local police officers work and where people can report crimes",
        facility_type="Safety and Security",
    ),
    Facilities(
        name="Fire Station",
        description="A building housing emergency equipment and personnel for firefighting",
        facility_type="Safety and Security",
    ),
    Facilities(
        name="Public Gym",
        description="A facility equipped with exercise machines and weights for physical fitness",
        facility_type="Recreation",
    ),
    Facilities(
        name="Municipal Office",
        description="An office where local government administrative activities take place",
        facility_type="Government",
    ),
    Facilities(
        name="Public Swimming Pool",
        description="A facility where individuals can swim, often overseen by lifeguards",
        facility_type="Recreation",
    ),
    Facilities(
        name="Post Office",
        description="A facility where mail is processed and sent, and where people can buy postage stamps, send packages, etc.",
        facility_type="Communication",
    ),
]


values_list = [
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (1, 6),
    (1, 7),
    (1, 8),
    (1, 9),
    (1, 10),
    (2, 1),
    (2, 2),
    (2, 3),
    (2, 4),
    (2, 5),
    (2, 6),
    (2, 7),
    (2, 8),
    (2, 9),
    (2, 10),
    (3, 1),
    (3, 2),
    (3, 3),
    (3, 4),
    (3, 5),
    (3, 6),
    (3, 7),
    (3, 8),
    (3, 9),
    (3, 10),
    (4, 1),
    (4, 2),
    (4, 3),
    (4, 4),
    (4, 5),
    (4, 6),
    (4, 7),
    (4, 8),
    (4, 9),
    (4, 10),
    (5, 1),
    (5, 2),
    (5, 3),
    (5, 4),
    (5, 5),
    (5, 6),
    (5, 7),
    (5, 8),
    (5, 9),
    (5, 10),
    (6, 1),
    (6, 2),
    (6, 3),
    (6, 4),
    (6, 5),
    (6, 6),
    (6, 7),
    (6, 8),
    (6, 9),
    (6, 10),
    (7, 1),
    (7, 2),
    (7, 3),
    (7, 4),
    (7, 5),
    (7, 6),
    (7, 7),
    (7, 8),
    (7, 9),
    (7, 10),
    (8, 1),
    (8, 2),
    (8, 3),
    (8, 4),
    (8, 5),
    (8, 6),
    (8, 7),
    (8, 8),
    (8, 9),
    (8, 10),
    (9, 1),
    (9, 2),
    (9, 3),
    (9, 4),
    (9, 5),
    (9, 6),
    (9, 7),
    (9, 8),
    (9, 9),
    (9, 10),
]


counties_to_add1 = [
    County(name="Orange", population=1393452, area=903),
    County(name="Seminole", population=471826, area=309),
    County(name="Lake County", population=367118, area=953),
    County(name="Osceola", population=375751, area=1325),
    County(name="Miami Dade", population=2716940, area=1898),
    County(name="Broward", population=1952778, area=1209),
    County(name="Palm Beach", population=1496770, area=1969),
    County(name="Hillsborough", population=1471968, area=1020),
    County(name="Pinellas", population=974996, area=274),
    County(name="Duval", population=957755, area=762),
    County(name="Lee", population=770577, area=785),
    County(name="Polk", population=724777, area=1798),
    County(name="Kings (Brooklyn)", population=2559903, area=69),
    County(name="Queens", population=2253858, area=108),
    County(name="New York (Manhattan)", population=1628706, area=22.7),
    County(name="Suffolk", population=1476601, area=912),
    County(name="Bronx", population=1472654, area=42),
    County(name="Nassau", population=1356924, area=285),
    County(name="Westchester", population=967506, area=432),
    County(name="Erie", population=918702, area=1044),
    County(name="Monroe", population=741770, area=657),
    County(name="Richmond (Staten Island)", population=476143, area=57),
]


weather_icons = {
    "clear sky": "☀️",
    "few clouds": "⛅",
    "scattered clouds": "🌥️",
    "broken clouds": "☁️",
    "overcast clouds": "🌥️",
    "mist": "🌫️",
    "haze": "🌫️",
    "smoke": "🌫️",
    "fog": "🌫️",
    "light intensity drizzle": "🌧️",
    "drizzle": "🌧️",
    "heavy intensity drizzle": "🌧️",
    "light intensity drizzle rain": "🌧️",
    "drizzle rain": "🌧️",
    "heavy intensity drizzle rain": "🌧️",
    "shower rain and drizzle": "🌧️",
    "heavy shower rain and drizzle": "🌧️",
    "shower drizzle": "🌧️",
    "light rain": "🌧️",
    "moderate rain": "🌧️",
    "heavy intensity rain": "🌧️",
    "very heavy rain": "🌧️",
    "extreme rain": "🌧️",
    "freezing rain": "❄️🌧️",
    "light intensity shower rain": "🌧️",
    "shower rain": "🌧️",
    "heavy intensity shower rain": "🌧️",
    "ragged shower rain": "🌧️",
    "light snow": "❄️🌨️",
    "snow": "❄️🌨️",
    "heavy snow": "❄️🌨️",
    "sleet": "❄️🌨️",
    "shower sleet": "❄️🌨️",
    "light rain and snow": "❄️🌨️",
    "rain and snow": "❄️🌨️",
    "light shower snow": "❄️🌨️",
    "shower snow": "❄️🌨️",
    "heavy shower snow": "❄️🌨️",
    "mist": "🌫️",
    "smoke": "🌫️",
    "haze": "🌫️",
    "sand/ dust whirls": "🌀",
    "fog": "🌫️",
    "sand": "🌫️",
    "dust": "🌫️",
    "volcanic ash": "🌋",
    "squalls": "🌬️",
    "tornado": "🌪️",
    "clear sky": "☀️",
    "light rain": "🌦️",
    "thunderstorm with rain": "⛈️🌧️",
    "thunderstorm with heavy rain": "⛈️🌧️",
    "thunderstorm with light drizzle": "⛈️🌧️",
    "thunderstorm with drizzle": "⛈️🌧️",
    "thunderstorm with heavy drizzle": "⛈️🌧️",
    "thunderstorm with hail": "⛈️🌨️",
    "thunderstorm with heavy hail": "⛈️🌨️",
    "thunderstorm with light rain": "⛈️🌦️",
    "thunderstorm with rain": "⛈️🌦️",
    "thunderstorm with heavy rain": "⛈️🌦️",
    "thunderstorm with light drizzle": "⛈️🌦️",
    "thunderstorm with drizzle": "⛈️🌦️",
    "thunderstorm with heavy drizzle": "⛈️🌦️",
    "thunderstorm with hail": "⛈️🌦️",
    "thunderstorm with heavy hail": "⛈️🌦️",
    "clear sky": "☀️",
    "cloudy sky": "☁️",
    "hurricane": "🌀",
    "cold": "❄️",
    "hot": "🔥",
    "windy": "💨",
    "hail": "🌨️",
}
