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

2. All the data is fetched in the properties tab. The user can scroll down and check the collection of properties. There are two nested tabs in  Properties: List and Add New Property. The List tab is, by default, where all data is displayed. By clicking the view button on a property card, users will be sent to a new view where only the selected property is shown. Also, the users can access more images, and a delete button is in the detail view. The user will be sent to the List tab by clicking the List button. The Add New Property tab is where the user adds new real estate properties in the database.

3. A table is shown in the Table tab. It contains information on seven attributes (id,  city, state, listing price,  square feet,  property type, and operation type). Users can sort the attributes by clicking on the table header. Additionally, users can search for a specific detail by typing in the search text box input located about the table.

4. Two statistics charts are shown in the Charts tab. A bar chart and a line chart show information about how properties prices in Texas state. If the user hovers over the graph, some information will be displayed.

<div align="center">

---

![how this app works](https://github.com/hcoco1/phase3_cli_click/blob/main/db_diagram.png?raw=true) 


 
---


</div>


### **Project Structure**

 Real Estate Site runs on a single page and has Eighteen  JSX components.
```
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── __pycache__
│   ├── test_fake_data.cpython-38.pyc
│   └── test_helpers.cpython-38.pyc
├── alembic.ini
├── lib
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── cli.cpython-38.pyc
│   │   ├── helpers.cpython-38.pyc
│   │   └── test_helpers.cpython-38.pyc
│   ├── cli.py
│   ├── db
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-38.pyc
│   │   │   ├── data.cpython-38.pyc
│   │   │   ├── display.cpython-38.pyc
│   │   │   ├── models.cpython-38.pyc
│   │   │   └── seed.cpython-38.pyc
│   │   ├── data.py
│   │   ├── display.py
│   │   ├── geodata.db
│   │   ├── models.py
│   │   ├── seed.py
│   │   └── seed_all_data.py
│   ├── debug.py
│   ├── helpers.py
│   ├── populate_association.py
│   └── user_interactions
│       ├── user_details.txt
│       ├── user_interaction.py
│       └── user_scores.txt
├── migrations
│   ├── README
│   ├── __pycache__
│   │   └── env.cpython-38.pyc
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       ├── __pycache__
│       │   └── e3fb3d80e214_initial_stage.cpython-38.pyc
│       └── e3fb3d80e214_initial_stage.py
└── requirements.txt

```

 

 

 
 
 Also, RES uses seven client-side routes (four nested). Users can navigate between routes using the navigation bar and the nested menu.
 
Component App:


```javascript
<Container>
  <Row>
    <Col lg>
      <NavigationBar />
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='charts' element={<PropertyCharts properties={properties} />}></Route>
        <Route path='search' element={<SearchTable properties={properties} />}></Route>
        <Route path='/properties/' element={<Properties />}>
          <Route path='list' element={<ListProperties properties={properties} onUpdate={handleCurrentProperty} />} />
          <Route path='add' element={<AddProperty onhandleAddProperty={handleAddProperty} setProperties={setProperties} property={currentProperty} />} />
          <Route path=':id' element={<PropertyDisplay properties={properties} property={currentProperty} onhandleDeletedProperty={handleDeletedProperty} />} />
          <Route path='*' element={<NoMatch />} />
        </Route>
      </Routes>
    </Col>
  </Row>
</Container>
```
Component NavigationBar:

```javascript
<Navbar collapseOnSelect expand="lg" className="bg-body-tertiary" sticky="top" >
  <Container>
    <Navbar.Brand>
      <Link className="linkNav" to="/">Home</Link>
    </Navbar.Brand>
    <Navbar.Toggle aria-controls="responsive-navbar-nav" />
    <Navbar.Collapse id="responsive-navbar-nav">
      <Nav className="me-auto">
        <NavLink id="RouterNavLink" className="linkNav" to="properties/list">Properties</NavLink>
        <NavLink id="RouterNavLink" className="linkNav" to="/search">Search</NavLink>
        <NavLink id="RouterNavLink" className="linkNav" to="charts">Charts</NavLink>
      </Nav>
    </Navbar.Collapse>
  </Container>
</Navbar>
```


Additionally, RES uses three RESTful routing conventions:

| Route   Name    | URL             | HTTP Verb | Description                |
|-----------------|-----------------|-----------|----------------------------|
| ListProperties  | properties/list | GET       | Display all properties     |
| AddProperty     | properties/add  | POST      | Add new property to db     |
| PropertyDisplay | properties/:id  | DELETE    | Delete a specific property |

---
### Backend Setup

**Real Estate Site (RES)**  makes GET, POST, and DELETE requests to the " properties " web database. The POST request is managed for a controlled form using a "react-hook-form" hook.

Database Structure



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




 Some of the dependencies of **Real Estate Site** are:

| #  	| Dependencies                               	|
|----	|--------------------------------------------	|
| 1  	|           "bootstrap": "^5.3.0",           	|
| 2  	|           "chart.js": "^4.3.0",            	|
| 3  	|           "mdb-react-ui-kit": "^6.1.0",    	|
| 4  	|           "mdb-ui-kit": "^6.4.0",          	|
| 5  	|           "modern-normalize": "^2.0.0",    	|
| 6  	|           "react-bootstrap": "^2.7.4",     	|
| 7  	|           "react-chartjs-2": "^5.2.0",     	|
| 8  	|           "react-dom": "^18.2.0",          	|
| 9  	|           "react-hook-form": "^7.45.0",    	|
| 10 	|           "react-icons": "^4.9.0",         	|
| 11 	|           "react-router-dom": "^6.13.0",   	|
| 12 	|           "react-table": "^7.8.0",         	|
| 13 	|           "react-table-plugins": "^1.3.4", 	|
| 14 	|           "react-table-sticky": "^1.1.3",  	|
| 15 	|           "semantic-ui-css": "^2.5.0",     	|
| 16 	|           "semantic-ui-react": "^2.1.4",   	|


##### **Challenges**

 1. Write a clean code / Use Folders to organize the components. 

 2. Responsive design.

 3. Update the state of the modal components.
