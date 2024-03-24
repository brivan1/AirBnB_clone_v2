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


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def one_state(id=None):
    """
    This funtion renders a HTML template that list a specified state route
    is hit with a specified id else all the states will be listed when the
    /states route is hit without a specified id
    """
    states = storage.all('State')
    if id:
        st = '{}.{}'.format('State', id)
        if st in states:
            states = states[st]
        else:
            states = None
    else:
        states = storage.all('State').values()
    return launch('9-states.html', id=id, states=states)


@app.teardown_appcontext
def teardown(self):
    """This function removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
