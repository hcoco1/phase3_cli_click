from lib.db.models import State, County, City, Facilities
from faker import Faker
import random
fake = Faker()
import random



# Define the number of records you want for each type
NUM_STATES = 5
NUM_COUNTIES = 10
NUM_CITIES_PER_STATE = 4
NUM_FACILITIES = 20

states_to_add = []
counties_to_add = []
cities_to_add = []
facilities_to_add = []

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

# Generate Counties
for _ in range(NUM_COUNTIES):
    county = County(
        name=fake.city(),
        population=random.randint(1000, 40000),
        area=random.uniform(100.0, 9000.0)
    )
    counties_to_add.append(county)

# Generate Facilities
facility_types = ["Education", "Healthcare", "Recreation", "Safety and Security", "Government", "Communication"]
for _ in range(NUM_FACILITIES):
    facility = Facilities(
        name=fake.company(),
        description=fake.sentence(),
        facility_type=random.choice(facility_types)
    )
    facilities_to_add.append(facility)


# New function to generate cities for states
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



states_to_play = [
    {
        "name":"Alabama",
        "abbreviation":"AL",
        "population":4903185,
        "capital":"Montgomery",
        "area":52420,
    },
    {
        "name":"Alaska",
        "abbreviation":"AK",
        "population":731545,
        "capital":"Juneau",
        "area":665384,
    },
    {
        "name":"Arizona",
        "abbreviation":"AZ",
        "population":7278717,
        "capital":"Phoenix",
        "area":113990,
    },
    {
        "name":"Arkansas",
        "abbreviation":"AR",
        "population":3017804,
        "capital":"Little Rock",
        "area":53179,
    },
    {
        "name":"California",
        "abbreviation":"CA",
        "population":39538223,
        "capital":"Sacramento",
        "area":163695,
    },
    {
        "name":"Colorado",
        "abbreviation":"CO",
        "population":5773714,
        "capital":"Denver",
        "area":104094,
    },
    {
        "name":"Connecticut",
        "abbreviation":"CT",
        "population":3565287,
        "capital":"Hartford",
        "area":5543,
    },
    {
        "name":"Delaware",
        "abbreviation":"DE",
        "population":973764,
        "capital":"Dover",
        "area":2489,
    },
    {
        "name":"Florida",
        "abbreviation":"FL",
        "population":21538187,
        "capital":"Tallahassee",
        "area":65758,
    },
    {
        "name":"Georgia",
        "abbreviation":"GA",
        "population":10617423,
        "capital":"Atlanta",
        "area":59425,
    },
    {
        "name":"Hawaii",
        "abbreviation":"HI",
        "population":1455271,
        "capital":"Honolulu",
        "area":10932,
    },
    {
        "name":"Idaho",
        "abbreviation":"ID",
        "population":1787065,
        "capital":"Boise",
        "area":83569
    },
    {
        "name":"Illinois",
        "abbreviation":"IL",
        "population":12671821,
        "capital":"Springfield",
        "area":57914,
    },
    {
        "name":"Indiana",
        "abbreviation":"IN",
        "population":6732219,
        "capital":"Indianapolis",
        "area":36420,
    },
    {
        "name":"Iowa",
        "abbreviation":"IA",
        "population":3155070,
        "capital":"Des Moines",
        "area":56273,
    },
    {
        "name":"Kansas",
        "abbreviation":"KS",
        "population":2913314,
        "capital":"Topeka",
        "area":82278,
    },
    {
        "name":"Kentucky",
        "abbreviation":"KY",
        "population":4467673,
        "capital":"Frankfort",
        "area":40408,
    },
    {
        "name":"Louisiana",
        "abbreviation":"LA",
        "population":4648794,
        "capital":"Baton Rouge",
        "area":52378,
    },
    {
        "name":"Maine",
        "abbreviation":"ME",
        "population":1344212,
        "capital":"Augusta",
        "area":35380,
    },
    {
        "name":"Maryland",
        "abbreviation":"MD",
        "population":6045680,
        "capital":"Annapolis",
        "area":12406,
    },
    {
        "name":"Massachusetts",
        "abbreviation":"MA",
        "population":6892503,
        "capital":"Boston",
        "area":10554,
    },
    {
        "name":"Michigan",
        "abbreviation":"MI",
        "population":9986857,
        "capital":"Lansing",
        "area":96714,
    },
    {
        "name":"Minnesota",
        "abbreviation":"MN",
        "population":5639632,
        "capital":"Saint Paul",
        "area":86936,
    },
    {
        "name":"Mississippi",
        "abbreviation":"MS",
        "population":2976149,
        "capital":"Jackson",
        "area":48432,
    },
    {
        "name":"Missouri",
        "abbreviation":"MO",
        "population":6137428,
        "capital":"Jefferson City",
        "area":69707,
    },
    {
        "name":"Montana",
        "abbreviation":"MT",
        "population":1068778,
        "capital":"Helena",
        "area":147040,
    },
    {
        "name":"Nebraska",
        "abbreviation":"NE",
        "population":1934408,
        "capital":"Lincoln",
        "area":77348,
    },
    {
        "name":"Nevada",
        "abbreviation":"NV",
        "population":3080156,
        "capital":"Carson City",
        "area":110572,
    },
    {
        "name":"New Hampshire",
        "abbreviation":"NH",
        "population":1359711,
        "capital":"Concord",
        "area":9349,
    },
    {
        "name":"New Jersey",
        "abbreviation":"NJ",
        "population":8882190,
        "capital":"Trenton",
        "area":8723,
    },
    {
        "name":"New Mexico",
        "abbreviation":"NM",
        "population":2117522,
        "capital":"Santa Fe",
        "area":121590,
    },
    {
        "name":"New York",
        "abbreviation":"NY",
        "population":19453561,
        "capital":"Albany",
        "area":54555,
    },
    {
        "name":"North Carolina",
        "abbreviation":"NC",
        "population":10488084,
        "capital":"Raleigh",
        "area":53819,
    },
    {
        "name":"North Dakota",
        "abbreviation":"ND",
        "population":762062,
        "capital":"Bismarck",
        "area":70698,
    },
    {
        "name":"Ohio",
        "abbreviation":"OH",
        "population":11689100,
        "capital":"Columbus",
        "area":44826,
    },
    {
        "name":"Oklahoma",
        "abbreviation":"OK",
        "population":3956971,
        "capital":"Oklahoma City",
        "area":69903,
    },
    {
        "name":"Oregon",
        "abbreviation":"OR",
        "population":4217737,
        "capital":"Salem",
        "area":98379,
    },
    {
        "name":"Pennsylvania",
        "abbreviation":"PA",
        "population":12801989,
        "capital":"Harrisburg",
        "area":46054,
    },
    {
        "name":"Rhode Island",
        "abbreviation":"RI",
        "population":1059361,
        "capital":"Providence",
        "area":1545,
    },
    {
        "name":"South Carolina",
        "abbreviation":"SC",
        "population":5148714,
        "capital":"Columbia",
        "area":32020,
    },
    {
        "name":"South Dakota",
        "abbreviation":"SD",
        "population":884659,
        "capital":"Pierre",
        "area":77116,
    },
    {
        "name":"Tennessee",
        "abbreviation":"TN",
        "population":6829174,
        "capital":"Nashville",
        "area":42144,
    },
    {
        "name":"Texas",
        "abbreviation":"TX",
        "population":28995881,
        "capital":"Austin",
        "area":268596,
    },
    {
        "name":"Utah",
        "abbreviation":"UT",
        "population":3271616,
        "capital":"Salt Lake City",
        "area":84897,
    },
    {
        "name":"Vermont",
        "abbreviation":"VT",
        "population":623989,
        "capital":"Montpelier",
        "area":9616,
    },
    {
        "name":"Virginia",
        "abbreviation":"VA",
        "population":8535519,
        "capital":"Richmond",
        "area":42775,
    },
    {
        "name":"Washington",
        "abbreviation":"WA",
        "population":7614893,
        "capital":"Olympia",
        "area":71298,
    },
    {
        "name":"West Virginia",
        "abbreviation":"WV",
        "population":1792147,
        "capital":"Charleston",
        "area":24230,
    },
    {
        "name":"Wisconsin",
        "abbreviation":"WI",
        "population":5822434,
        "capital":"Madison",
        "area":65496,
    },
    {
        "name":"Wyoming",
        "abbreviation":"WY",
        "population":578759,
        "capital":"Cheyenne",
        "area":97813,
    }
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

