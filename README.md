# R&I Software



### Installing Dependencies for the Backend

1. **Python 3.9** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3.9/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the project directory and running:
```bash
# On Windows:
py -m pip install -r requirements.txt
# On Linux:
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


<!-- 4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.  -->


## Database Setup
Set database url as an environment variable:
```bash
# On Windows:
set DATABASE_URL=dialect+driver://username:password@host:port/database;
# On Linux:
export DATABASE_URL=dialect+driver://username:password@host:port/database;
```
or insert database url to `config.cfg` file. If none of them is provided, SQLite will be applied.

## Running the server

First of all, activate venv by running this command in the project directory:

```bash
# On Windows:
venv\Scripts\activate
# On Linux:
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
```


### Run APP API:
```bash
# On Windows:
py manage.py
# On Linux:
python3 manage.py
```

You can see app running on http://127.0.0.1:5000.

#### **WARNING!!!** The React project can be configured to redirect any requests it receives on its port 3000 that it does not understand into another server. This is configured simply by adding a proxy key at the bottom `package.json`:
```json
{

  /* ... leave all other configuration options alone ... */

  "proxy": "http://localhost:5000"
}
```


# Rest API
## Getting started
* There is a sample Postman test collection `server\tests\risoftware.postman_collection.json` so you can try your first requests.
## Endpoints
### 1. GET http://127.0.0.1:5000/api/api - Check API is running.
* Sample response
```json
{
    "description": "Checking API running.",
    "ok": true,
    "result": {
        "api_working": true
    }
}
```


### 2. POST http://127.0.0.1:5000/api/login - Login user.
* Sample data:
```json
{
    "email": "baby",
    "password": "baby"
}
```
* Sample response:
```json
{
    "ok": true,
    "description": "Logged in successfully",
    "result": {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2ODg4NTIxNywianRpIjoiMDQ4YjcwMTgtZGU3Yy00MjMxLThjOGUtZTUyNzcwMzI4ZDM2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImQxNTU2ZGVlZjZiMjQwMDU4NDY0NDk3MjYwNWFlZmRjIiwibmJmIjoxNjY4ODg1MjE3LCJleHAiOjE2Njg4ODYxMTd9.8YIeMoPr3mBxBw2NP8WK_1ezZOC38614glzwL7BD9RM",
        "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2ODg4NTIxNywianRpIjoiMjhkMGFkMjItNzg2OC00OTUxLTg0ZDktZmMxMTA4OGEwNmI4IiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiJkMTU1NmRlZWY2YjI0MDA1ODQ2NDQ5NzI2MDVhZWZkYyIsIm5iZiI6MTY2ODg4NTIxNywiZXhwIjoxNjcxNDc3MjE3fQ.hbO3F0Li9VCBSKgP809cA3PrHOpM3Jiteo94iiFAt8Y"
    }
}
```

### 3. POST http://127.0.0.1:5000/api/signup - SignUp user.
* Sample data:
```json
{
    "email": "newuser3",
    "password": "new3",
    "first_name": "newusersfirstname"
}
```
* Sample response:
```json
{
    "ok": true,
    "description": "Created successfully.",
    "result": {
        "external_id": "c9199da670294ae7babc18d853dc1d02",
        "email": "newuser3"
    }
}
```


### 4. GET http://127.0.0.1:5000/api/whoami - Who Am I endpoint (current_user).
* Authorization: Bearer Token (access token)
* Sample response:
```json
{
    "ok": true,
    "description": "Got user details.",
    "result": {
        "external_id": "1f32831892174fc09838254164c6315a",
        "email": "newuser1",
        "first_name": "newusersfirstname",
        "last_name": null,
        "company_name": null,
        "phone_number": null,
        "role": "user",
        "is_admin": false
    }
}
```


### 5. GET http://127.0.0.1:5000/api/refresh - Refresh token.
* Authorization: Bearer Token (refresh token)
* Sample response
```json
{
    "ok": true,
    "description": "",
    "result": {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2ODg4NTU3OCwianRpIjoiZmY1NmIyNzAtZjcwNS00MzY5LWE4MGItZTI5ZDMxMmQ5Y2M5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImQxNTU2ZGVlZjZiMjQwMDU4NDY0NDk3MjYwNWFlZmRjIiwibmJmIjoxNjY4ODg1NTc4LCJleHAiOjE2Njg4ODY0Nzh9.jnbnZL2ynziEsiAdR3IUF-mA57yFXkCJV_AnSNaaS9U"
    }
}
```









## APP Resources:
* APP on webserver: https://

