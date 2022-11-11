# R&I Software



### Installing Dependencies for the Backend

1. **Python 3.9** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3.9/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the project directory and running:
```bash
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
export DATABASE_URL='dialect+driver://username:password@host:port/database';
```
or insert database url to `config.cfg` file.

## Running the server

First of all, activate venv by running this command in the project directory:
```
venv\Scripts\activate
```

### Run APP API:
* On Windows:
```bash
py manage.py
```
* On Linux:
```bash
python3 manage.py
```

You can see app running on http://127.0.0.1:5000

### **WARNING!!!** The React project can be configured to redirect any requests it receives on its port 3000 that it does not understand into another server. This is configured simply by adding a proxy key at the bottom `package.json`:
```
{

  ... leave all other configuration options alone ...

  "proxy": "http://localhost:5000"
}
```

## APP Resources:
* APP on webserver: https://



# Rest API
## Endpoints
### 1. GET http://127.0.0.1:5000/api/api - Check API is running.
Sample response
```
{
  "ok": true,
  "result": {
    "api_working": true
  }
}
```

### 2. GET http://127.0.0.1:5000/api/users - Get all users information.
Sample response
```
{
  "ok": true,
  "result": {
    "users": [
      {
        "admin": false,
        "company_name": null,
        "email": "baby@mail.com",
        "first_name": "Baby",
        "id": 1,
        "last_name": null,
        "phone_number": null,
        "registered_on": "Mon, 07 Nov 2022 23:40:21 GMT",
        "role": "user"
      }
    ]
  }
}
```

### 3. ...




