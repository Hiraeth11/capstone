# Capstone 

## Motivation

This is my Final Project in the Udacity Full Stack Developer Nanodegree Program

It combines all the skills learned from the course. 

These Skills consist of:
- SQL and Data Modelling of the Web 
    - using SQLAlchemy to perform CRUD Operations and create relational database models
- API Development and Documentation
- Identity and Access Management
    - Implementing Role Based Access Control with Auth0 and JWT Tokens 
- Server Deployment by deploying the application to Heroku


#### URL of Application

This application is deployed to heroku at https://full-stack-developer-capstone.herokuapp.com/

#### Instructions to set up authentication

Token for Executive Producer:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imh3VXZlWTVFTl9ndExXNzV5dXNfeCJ9.eyJpc3MiOiJodHRwczovL2Rldi15OTZ5NWc3ci5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzNmI4YTk0ZWU1MDMwMDZkNjc3NWJlIiwiYXVkIjoibW92aWUiLCJpYXQiOjE1OTc0Mjk2OTgsImV4cCI6MTU5NzUxNjA5OCwiYXpwIjoidlZ5Szk3M3pudHIybU5jU2drb1VjcWN4YXl1ZUZpR1oiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.GRIeB6ynNSHqw-OKjpwnq9bDucXmGd8XQbcQ9gpq8GoC9WFDyYn07wqX6RVLoe4-SldQvpD3GoAni2aJRWf84dNU9WgmCGKIqieneitM31SjVWY9Oe0ocge10TrpkQ5im7oT14KWVskT_CUaMqVmttK7Cd4tl14UrvJvC-iVnRZ_ktZUa_I2hpCcQsuYaVj4lSLUjbi0I57xxgdJSrq9tD-zrmj9kmQZ4H18vZnYfHwOAXPnYh2OqwZDPx1tN7ip9drz_Nvibl-HV4ckvWVneuF71JSv7RXj-ObZGFheSKO8gR7YzyCkKLODW_pqHNWRqxyXfL0rfvrfPnKtnGZxEA

Token for Casting Director = 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imh3VXZlWTVFTl9ndExXNzV5dXNfeCJ9.eyJpc3MiOiJodHRwczovL2Rldi15OTZ5NWc3ci5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzNmI4ODcyOTkzM2MwMDY3M2JkMTIwIiwiYXVkIjoibW92aWUiLCJpYXQiOjE1OTc0Mjk4MjcsImV4cCI6MTU5NzUxNjIyNywiYXpwIjoidlZ5Szk3M3pudHIybU5jU2drb1VjcWN4YXl1ZUZpR1oiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.FGvcemKG66Af6F52FuwTrHtVx_MjcNTh4SiLkvQc4X8QOnLgX_SLUn05q9ceq-Vim9faLlWc5_DXJu-l34q9M1fAH8SEngq6UgfrN37lRAhPEvwK2RKpMYWppAHrr6SAc5UOpdFItQutckIuZw3TCxqebY3OG8vw8F6YSgXoivDTuQoWlgxpiylmUhjYz5z1U91Qtx-stzIEocOUAAywdtYix3kd3KD0vSlKpcqjt2YEG1idexFL61J_uJj9POdyCC5oacBNFOCp_hYOkYDbth8I--ud_33sp2NpaARdA3Gm1LDMK0SROb8cmT26qEKbMBYk24TC-wkNRfMRycLQkA

Token for Casting Assistant = 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imh3VXZlWTVFTl9ndExXNzV5dXNfeCJ9.eyJpc3MiOiJodHRwczovL2Rldi15OTZ5NWc3ci5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzNmI4NjcxNzA0YWYwMDZkZGZkZDU5IiwiYXVkIjoibW92aWUiLCJpYXQiOjE1OTc0Mjk4NjcsImV4cCI6MTU5NzUxNjI2NywiYXpwIjoidlZ5Szk3M3pudHIybU5jU2drb1VjcWN4YXl1ZUZpR1oiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.ocbjr4CYpyhwGDhGI6GF3fl8C1ZAUK2gB3YjqD9Dqdxmedl9Cl-3SMPoSmt0qOu6O9OIOteSC0L1sjbWigq62pP_s902g5LPyT_3vp0knLg2ZdwKEfpCqljX5hDWmbB0wh6F10xarFxoagM06BXqLATq4HwcTgeG1P5PVc9uMMluy-U7PIP2a1YlzUuAY1mY-T85aFFnG_PMLAfP3Z1rmrwUF39FmeGaSvUo0b8zxTprng2qQ2WG56JkcyebNWtCKkT1jNNl81onyqD9wzXm1aW5hrLps8RDyTlRCZUGNPFIMAKw8miyhn5nlvMeYs3V9oDY301AYRTdJPToPZ5_5A

### Installing Dependencies


#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```
##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the postgres database. 

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.


## Running the Server Locally



## API Documentation

### Roles and Permission
There are three different roles with the following permissions
- Casting Assistant
    - get:movies
    - get:actors
- Casting Director
    - get:movies
    - get:actors
    - post:actors
    - delete:actors
    - patch:actors
    - patch:movies
- Executive Producer
    - get:movies
    - get:actors
    - post:actors
    - post:movies 
    - delete:actors
    - delete:movies
    - patch:actors
    - patch:movies

### Endpoints

#### GET '/movies'
- General:
    - Fetches a list of all movies in database
    - Request Arguments: None
    - Returns: a list of formatted movie objects and the success value
- Authentication:
    - Requires a valid Bearer JWT Token included include in Authorization Header
- Sample Request: 
    ```
    curl http://localhost:5000/movies \
    -H "Authorization: Bearer {insert valid jwt token}"
    ```
- Sample Response:   
    ```
    {
        "movies": [
            {
                "id": 1,
                "release_date": "Wed, 01 Jan 2020 00:00:00 GMT",
                "title": "test"
            }
        ],
        "success": true
    }
    ```
#### GET '/actors'
- General:
    - Description: Fetches a list of all actors in database
    - Request Arguments: None
    - Returns: 
        - a list of formatted actor objects 
        - success value
- Authentication:
    - Requires a valid Bearer JWT Token included include in Authorization Header
- Sample Request: 
    ```
    curl http://localhost:5000/actors \
    -H "Authorization: Bearer {insert valid jwt token}"
    ```
- Sample Response:
    ```
    {
        "actors": [
            {
                "age": 32,
                "gender": "Male",
                "id": 1,
                "name": "first actor"
            }
        ],
        "success": true
    }

    ```

#### POST '/movies'
- General:
    - Description: a new movie is created
    - Request Arguments: None
    - Returns: 
        - created movie 
        - success value
- Authentication:
    - Requires a valid Bearer JWT Token included include in Authorization Header
- Sample Request:
    ```
    curl http://localhost:5000/movies -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer {insert valid jwt token}" \
    -d '{"title":"Movie title name", "release_date": "2019-01-01"}'
    ``` 
- Sample Response:
    ```
        {
            "new_movie":
            {
                "id":13,
                "release_date":"Tue, 01 Jan 2019 00:00:00 GMT",
                "title":"Movie title name"
            },
            "success":true
        }
    ```

#### POST '/actors'
- General:
    - Description: a new actor is created
    - Request Arguments: None
    - Returns: 
        - created actor
        - success value
- Authentication:
    - Requires a valid Bearer JWT Token included include in Authorization Header
- Sample Request:
    ```
    curl http://localhost:5000/actors -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer {insert valid jwt token}" \
    -d '{
            "name": "actor name",
            "age": 32,
            "gender": "Female"
        }'
    ``` 
- Sample Response
    ```
    {
        "new_actor":
            {
                "age":32,
                "gender":"Female",
                "id":20,
                "name":"actor name"
            },
        "success":true
    }
    ```

#### DELETE '/movies/{movie_id}'
- General:
    - Description: Deletes the movie specifed 
    - Request Arguments: 
        - movie_id - the id of the movie to be delete
    - Returns 
        - deleted movie 
        - success value
- Authentication:
    - Requires a valid Bearer JWT Token included include in Authorization Header
- Sample Request:
    ```
    curl http://localhost:5000/movies/13 -X DELETE \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer {insert valid jwt token}"
    ```
- Sample Response:
    ```
         {
            "new_movie":
            {
                "id":13,
                "release_date":"Tue, 01 Jan 2019 00:00:00 GMT",
                "title":"Movie title name"
            },
            "success":true
        }
    ```
#### DELETE '/actors/{actor_id}'
- General:
    - Description: Deletes the actor specifed 
    - Request Arguments: 
        - actor_id - the id of the actor to be delete
    - Returns 
        - deleted actor 
        - success value
- Authentication:
    - Requires a valid Bearer JWT Token included include in Authorization Header


- Sample Request: 
    ```
    curl http://localhost:5000/actors/20 -X DELETE \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer {insert valid jwt token}"
    ```
- Sample Response:
    ```
    {
        "new_actor":
            {
                "age":32,
                "gender":"Female",
                "id":20,
                "name":"actor name"
            },
        "success":true
    }
    ```

#### PATCH '/movies/{movie_id}'
- General:
    - Description: Updates the specified movie's details which are included in the body of the request
    - Request Arguments: 
        - movie_id - the id of the movie to be updated
    - Returns:
        - updated movie
        - success value
- Authentication:
    - Requires a valid Bearer JWT Token included include in Authorization Header
- Sample Request:
    ```
    curl http://localhost:5000/movies/12 -X PATCH \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer {insert valid jwt token}" \
    -d '{"title": "updated title"}'
    ```
- Sample Response:
    ```
    {
        "movie":
        {
            "id":12,
            "release_date":"Wed, 01 Jan 2020 00:00:00 GMT",
            "title":"updated title"
        },
        "success":true
        }

    ```

#### PATCH '/actors/{actor_id}'
- General:
    - Description: Updates the specified actor's details which are included in the body of the request
    - Request Arguments: 
        - actor_id - the id of the actor to be updated
    - Returns: 
        - updated actor 
        - success value
- Authentication:
    - Requires a valid Bearer JWT Token included include in Authorization Header
- Sample Request:
   ```
    curl http://localhost:5000/actors/11 \
    -X PATCH \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer {insert valid jwt token}" \
    -d '{"name": "updated name"}'
    ```
- Sample Response:
    ```
    {
        "actor":
        {
            "age":32,
            "gender":"Female",
            "id":11,
            "name":"updated name"
        },
        "success":true
    }
    ```
