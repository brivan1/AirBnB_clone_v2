#!/usr/bin/python3
"""
Python Flask script that starts a web application and is listening on port 5000
with ip 0.0.0.0
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Function that returns “Hello HBNB!” from the root route
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """
    Function that returns "HBNB when you navigate to /hbnb route
    """
    return "HBNB"


@app.route("/c/<text>/", strict_slashes=False)
def hello_c(text):
    """
    Function that accepts a parameter in the C route and displays the content
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python/<text>/", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python_route(text="is cool"):
    """
    Function that returns a default value when no parameter is supplied
    to the python route else displays the parameter supplied
    """
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
