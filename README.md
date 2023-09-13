# CRUD REST API with SQLite Database
![image](https://github.com/Sakindeb/Backend/assets/116188961/6f1bde38-16d1-449d-80ab-4b3a9e7683b0)

This project is a simple REST API built with Flask, allowing basic CRUD operations on a "person" resource. It uses an SQLite database to store person information.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Creating a Person](#creating-a-person)
  - [Reading a Person](#reading-a-person)
  - [Updating a Person](#updating-a-person)
  - [Deleting a Person](#deleting-a-person)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Documentation](#documentation)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

To run this project, you'll need:

- Python 3.x
- Flask (install via `pip install Flask`)
- Flask-SQLAlchemy (install via `pip install Flask-SQLAlchemy`)

### Installation

 Clone the repository:

   ```bash
   git clone https://github.com/Sakindeb/Backend.git

```
Create a virtual environment
```bash
$ virtualenv .venv
```

 Activate the virtual environment
```bash
$ source .venv/bin/activate
```

 Install the dependencies
```
$ pip install -r requirements.txt
```
### Running the app
* Run the app
```
$ python app.py
```

And finally, the application will run on the following URL: http://127.0.0.1:5000
## Usage
# Creating a Person
To create a new person, send a POST request to the /api/person endpoint with a JSON payload containing the person's name.
```
$ curl -X POST -H "Content-Type: application/json" -d '{"name": "Sakin Deborah"}' http://localhost:5000/api/person

```
# Reading a Person
To retrieve a person's details, send a GET request to the /api/person/{person_id} endpoint, where {person_id} is the ID of the person you want to retrieve.
```
$ curl http://localhost:5000/api/person/1

```
# Updating a Person
To update a person's details, send a PUT request to the /api/person/{person_id} endpoint with a JSON payload containing the updated name.

Example:
```
$ curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Name"}' http://localhost:5000/api/person/1

```
# Deleting a Person
To delete a person, send a DELETE request to the /api/person/{person_id} endpoint, where {person_id} is the ID of the person to delete.

Example:
```
$ curl -X DELETE http://localhost:5000/api/person/1

```


### API Endpoints
- POST /api/person: Create a new person.
- GET /api/person/{person_id}: Retrieve a person's details by ID.
- PUT /api/person/{person_id}: Update a person's details by ID.
- DELETE /api/person/{person_id}: Delete a person by ID.


### Testing
You can test the API using tools like Postman or by running test scripts. Make sure to test all CRUD operations to ensure they work as expected.

### Documentation
For detailed documentation on API requests and responses, refer to the DOCUMENTATION.md file in this repository.

### Deployment
You can deploy this API to a server of your choice. Ensure you have a production-ready database setup and configure the necessary environment variables.

### Contributing
Contributions are welcome! Please follow the contribution guidelines in this repository.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
