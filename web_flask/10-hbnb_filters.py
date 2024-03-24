#!/usr/bin/python3
"""
Python Flask script that starts a web application and is listening on port 5000
with ip 0.0.0.0
"""
from models import storage
from models.amenity import Amenity
from models.city import City
from models.state import State
from flask import Flask
from flask import render_template as launch

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)

def airbnb_filters():
    """
    This funtion renders a HTML template when the /hbnb_filters route is hit
    """
    states = storage.all('State').values()
    cities = storage.all('City').values()
    amenities = storage.all('Amenity').values()

    return launch('10-hbnb_filters.html', **locals())


@app.teardown_appcontext
def teardown(self):
    """This function removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
