<div align="center"><h1>Ivan Arias. Full-Stack Engineering Student.</h1></div>

<div id="badges" align="center">
  <a href="https://www.linkedin.com/in/arias-ivan-hcoco1/">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  <a href="https://www.youtube.com/channel/UCban0ilP3jBC9rdmL-fPy_Q">
    <img src="https://img.shields.io/badge/YouTube-red?style=for-the-badge&logo=youtube&logoColor=white" alt="Youtube Badge"/>
  </a>
  <a href="https://twitter.com/hcoco1">
    <img src="https://img.shields.io/badge/Twitter-blue?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter Badge"/>
  </a>
</div>  


## Phase 3 Project: Database Tool.

##### Phase 2 Project repository link: https://github.com/hcoco1/phase3_cli_click



### Project Pitch

**Database Tool (DT)** is a SQLALCHEMY/SQLITE3/CLICK command line interface (CLI) designed to manage US entities like states, cities, and counties.  Users can effortlessly navigate through a color-coded menu, making CRUD (Create, Read, Update, Delete) operations more intuitive than ever. Whether you're looking to display all entities, add a new city, or even fetch the latest weather updates for it. Additionally, the tool integrates advanced features such as updating city coordinates and instant weather insights.

## Installation instructions:
1. Fork and clone this repository.
2. Open the project directory in your terminal.
3. Install the dependencies using the following commands:
```
    pipenv install
    pipenv shell
    pip install -r requirements.txt
```
4. Once all of the dependencies have been installed, you must navigate to the lib folder and start the CLI using the following command:
```
    python user.py
```


## How to navigate in RES:

 Users can access the app data through four main links in the navigation bar: Home, Properties, Tables, and Charts.

1. Once the page load, the home page shows a few images and some information about real estate.



<div align="center">

---
![how this app works](https://github.com/hcoco1/phase3_cli_click/blob/main/cli_gif.gif?raw=true) 

---

</div>


### **Project Structure**
```
.
├── LICENSE
├── NOTES.md
├── Pipfile
├── Pipfile.lock
├── README.md
├── __init__.py
├── __pycache__
│   ├── cli.cpython-38.pyc
│   ├── data.cpython-38.pyc
│   ├── display.cpython-38.pyc
│   ├── helpers.cpython-38.pyc
│   ├── models.cpython-38.pyc
│   ├── seed.cpython-38.pyc
│   └── user_interaction.cpython-38.pyc
├── alembic.ini
├── blog
│   └── README.md
├── cli_gif.gif
├── db_diagram.png
├── geodata.db
├── lib
│   ├── __pycache__
│   │   ├── display.cpython-38.pyc
│   │   ├── game.cpython-38.pyc
│   │   ├── helpers.cpython-38.pyc
│   │   ├── start.cpython-38.pyc
│   │   ├── test_db.cpython-38.pyc
│   │   └── weather.cpython-38.pyc
│   ├── db
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-38.pyc
│   │   │   ├── data.cpython-38.pyc
│   │   │   ├── models.cpython-38.pyc
│   │   │   └── seed.cpython-38.pyc
│   │   ├── data.py
│   │   ├── geodata.db
│   │   ├── models.py
│   │   └── seed.py
│   ├── display.py
│   ├── game.py
│   ├── helpers.py
│   ├── others
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   └── aggregate_methods.cpython-38.pyc
│   │   ├── aggregate_methods.py
│   │   ├── associate_methods.py
│   │   ├── debug.py
│   │   ├── populate_associations.py
│   │   └── remove_cache.py
│   ├── start.py
│   ├── test_db.py
│   ├── user.py
│   ├── user_details.txt
│   ├── user_scores.txt
│   └── weather.py
├── migrations
│   ├── README
│   ├── __pycache__
│   │   └── env.cpython-38.pyc
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       ├── 006895a8c21a_add_fk_to_classes.py
│       ├── __pycache__
│       │   ├── 006895a8c21a_add_fk_to_classes.cpython-38.pyc
│       │   ├── c5fcbfbc59f7_states_and_counties_related.cpython-38.pyc
│       │   └── e3fb3d80e214_initial_stage.cpython-38.pyc
│       ├── c5fcbfbc59f7_states_and_counties_related.py
│       └── e3fb3d80e214_initial_stage.py
├── requirements.txt
└── video
    └── README.md

13 directories, 61 files
```




 

### Database schema

**One-to-Many Relationships**:

State and County: One state can have multiple counties. This is established using the state_id foreign key in the County class and the counties relationship in the State class.
State and City: Similarly, one state can have multiple cities. This is established using the state_id foreign key in the City class and the cities relationship in the State class.
County and City: One county can have multiple cities. This is set up using the county_id foreign key in the City class and the cities relationship in the County class.

**Many-to-Many Relationships**:

City and Facilities: A city can have multiple facilities and a facility can be present in multiple cities. The City and Facilities have a many-to-many relationship, which is achieved using the association_table as a secondary table. This table doesn't have its own ORM class representation; instead, it's a  table representation in SQLAlchemy.
The relationship function uses a secondary parameter to specify the association_table, creating the many-to-many linkage.


 <div align="center">

---
![how this app works](https://github.com/hcoco1/phase3_cli_click/blob/main/db_diagram.png?raw=true) 
---
</div>



```console

CREATE TABLE IF NOT EXISTS "Cities" (
        id INTEGER NOT NULL, 
        name VARCHAR(255), 
        population INTEGER, 
        area INTEGER, 
        latitude FLOAT, 
        longitude FLOAT, 
        county_name VARCHAR(255), 
        PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS "Counties" (
        id INTEGER NOT NULL, 
        name VARCHAR(255), 
        population INTEGER, 
        area FLOAT, 
        PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS "Facilities" (
        id INTEGER NOT NULL, 
        name VARCHAR(255), 
        description VARCHAR(255), 
        facility_type VARCHAR(255), 
        PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS "States" (
        id INTEGER NOT NULL, 
        name VARCHAR(255), 
        abbreviation VARCHAR(255), 
        population INTEGER, 
        capital VARCHAR(255), 
        area FLOAT, 
        PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS "CityFacilityAssociation" (
        city_id INTEGER, 
        facility_id INTEGER, 
        FOREIGN KEY(city_id) REFERENCES "Cities" (id), 
        FOREIGN KEY(facility_id) REFERENCES "Facilities" (id)
);
```






#### **Challenges**

 1. 

 2. 

 3. 
