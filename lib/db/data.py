from models import State, County, City, Facilities
from faker import Faker
import random
fake = Faker()


# Define the number of records you want for each type
NUM_STATES = 5
NUM_COUNTIES = 300
NUM_CITIES_PER_STATE = 4
NUM_FACILITIES = 20

states_to_add = []
counties_to_add = []
cities_to_add = []
facilities_to_add = []

"""
# Generate States
for _ in range(NUM_STATES):
    state = State(
        name=fake.state(),
        abbreviation=fake.state_abbr(),
        population=random.randint(1500, 50000),
        capital=fake.city(),
        area=random.uniform(500.0, 10000.0)
    )
    states_to_add.append(state)
"""


# Generate Counties
for _ in range(NUM_COUNTIES):
    county = County(
        name=fake.city(),
        population=random.randint(1000, 40000),
        area=random.uniform(100.0, 9000.0)
    )
    counties_to_add.append(county)

# Generate Facilities
facility_name = ["Public School", "Public Library", "Public Hospital", "Community Park", "Police Station", "Fire Station"]
facility_description = ["An educational institution for children aged 5-18", "A facility where people can borrow books and access digital resources", "A healthcare institution providing treatment with specialized medical and nursing staff", "A green area reserved for recreational activities, often equipped with playgrounds, benches, and sports fields", "A building where local police officers work and where people can report crimes", "A building housing emergency equipment and personnel for firefighting"]
facility_types = ["Education", "Healthcare", "Recreation", "Safety", "Government", "Communication"]
for _ in range(NUM_FACILITIES):
    facility = Facilities(
        name=random.choice(facility_name),
        description=random.choice(facility_description),
        facility_type=random.choice(facility_types)
    )
    facilities_to_add.append(facility)

    """# New function to generate cities for states
def generate_cities_for_states(session):
    cities = []
    for state in session.query(State).all():
        for _ in range(NUM_CITIES_PER_STATE):
            city = City(
                name=fake.city(),
                population=random.randint(100, 20000),
                area=random.randint(10, 2000),
                latitude=fake.latitude(),
                longitude=fake.longitude(),
                state_id=state.id,
                county_id=random.choice(session.query(County).all()).id
            )
            print(city)  # Debugging line
            cities.append(city)
    return cities
    """




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
        name="Idaho", abbreviation="ID", population=1787065, capital="Boise", area=83569
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

cities_to_add=[
        City(name='Montgomery', population=198525, area=159.8, latitude=0, longitude=0, state_id=1),
        City(name='Juneau', population=32113, area=2716.7, latitude=0, longitude=0, state_id=2),
        City(name='Phoenix', population=1680992, area=517.6, latitude=0, longitude=0, state_id=3),
        City(name='Little Rock', population=197312, area=116.2, latitude=0, longitude=0, state_id=4),
        City(name='Sacramento', population=513624, area=97.9, latitude=0, longitude=0, state_id=5),
        City(name='Denver', population=727211, area=153.3, latitude=0, longitude=0, state_id=6),
        City(name='Hartford', population=122105, area=17.3, latitude=0, longitude=0, state_id=7),
        City(name='Dover', population=38079, area=22.4, latitude=0, longitude=0, state_id=8),
        City(name='Tallahassee', population=194500, area=95.7, latitude=0, longitude=0, state_id=9),
        City(name='Atlanta', population=506811, area=133.5, latitude=0, longitude=0, state_id=10),
        City(name='Honolulu', population=345064, area=68.4, latitude=0, longitude=0, state_id=11),
        City(name='Boise', population=228959, area=63.8, latitude=0, longitude=0, state_id=12),
        City(name='Springfield', population=114230, area=54, latitude=0, longitude=0, state_id=13),
        City(name='Indianapolis', population=876384, area=361.5, latitude=0, longitude=0, state_id=14),
        City(name='Des Moines', population=214237, area=75.8, latitude=0, longitude=0, state_id=15),
        City(name='Topeka', population=125310, area=56, latitude=0, longitude=0, state_id=16),
        City(name='Frankfort', population=27679, area=14.7, latitude=0, longitude=0, state_id=17),
        City(name='Baton Rouge', population=220236, area=76.8, latitude=0, longitude=0, state_id=18),
        City(name='Augusta', population=18681, area=55.4, latitude=0, longitude=0, state_id=19),
        City(name='Annapolis', population=39174, area=6.73, latitude=0, longitude=0, state_id=20),
        City(name='Boston', population=692600, area=89.6, latitude=0, longitude=0, state_id=21),
        City(name='Lansing', population=118210, area=35, latitude=0, longitude=0, state_id=22),
        City(name='Saint Paul', population=308096, area=52.8, latitude=0, longitude=0, state_id=23),
        City(name='Jackson', population=160628, area=104.9, latitude=0, longitude=0, state_id=24),
        City(name='Jefferson City', population=42838, area=27.3, latitude=0, longitude=0, state_id=25),
        City(name='Helena', population=3215, area=14, latitude=0, longitude=0, state_id=26),
        City(name='Lincoln', population=289102, area=74.6, latitude=0, longitude=0, state_id=27),
        City(name='Carson City', population=55916, area=143.4, latitude=0, longitude=0, state_id=28),
        City(name='Concord', population=43627, area=64.3, latitude=0, longitude=0, state_id=29),
        City(name='Trenton', population=83203, area=7.66, latitude=0, longitude=0, state_id=30),
        City(name='Santa Fe', population=84683, area=37.3, latitude=0, longitude=0, state_id=31),
        City(name='Albany', population=96460, area=21.4, latitude=0, longitude=0, state_id=32),
        City(name='Raleigh', population=474069, area=114.6, latitude=0, longitude=0, state_id=33),
        City(name='Bismarck', population=73529, area=26.9, latitude=0, longitude=0, state_id=34),
        City(name='Columbus', population=898553, area=210.3, latitude=0, longitude=0, state_id=35),
        City(name='Oklahoma City', population=655057, area=620.3, latitude=0, longitude=0, state_id=36),
        City(name='Salem', population=174365, area=45.7, latitude=0, longitude=0, state_id=37),
        City(name='Harrisburg', population=49528, area=8.11, latitude=0, longitude=0, state_id=38),
        City(name='Providence', population=179883, area=18.5, latitude=0, longitude=0, state_id=39),
        City(name='Columbia', population=131674, area=125.2, latitude=0, longitude=0, state_id=40),
        City(name='Pierre', population=13646, area=13, latitude=0, longitude=0, state_id=41),
        City(name='Nashville', population=670820, area=525.9, latitude=0, longitude=0, state_id=42),
        City(name='Austin', population=978908, area=305.1, latitude=0, longitude=0, state_id=43),
        City(name='Salt Lake City', population=200567, area=109.1, latitude=0, longitude=0, state_id=44),
        City(name='Montpelier', population=7855, area=10.2, latitude=0, longitude=0, state_id=45),
        City(name='Richmond', population=230436, area=60.1, latitude=0, longitude=0, state_id=46),
        City(name='Olympia', population=46478, area=16.7, latitude=0, longitude=0, state_id=47),
        City(name='Charleston', population=46536, area=31.6, latitude=0, longitude=0, state_id=48),
        City(name='Madison', population=259680, area=68.7, latitude=0, longitude=0, state_id=49),
        City(name='Cheyenne', population=64235, area=21.1, latitude=0, longitude=0, state_id=50)
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

