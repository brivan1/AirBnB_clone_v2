#!/usr/bin/python3
"""
Python Flask script that starts a web application and is listening on port 5000
with ip 0.0.0.0
"""
from models import storage
from models.state import State
from flask import Flask
from flask import render_template as launch

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_states():
    """
    This funtion renders a HTML template that list all the states when
    the /state_list route is reached
    """
    return launch('7-states_list.html',
                  states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """This function removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
