#!/usr/bin/python3
"""
A Python Flask script that starts a web application listening on port 5000
with ip 0.0.0.0
"""
from flask import Flask
from flask import render_template as launch

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


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    """
    Function that returns a number when a numeric parameter is passed to route
    /number
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def n_route_temp(n):
    """
    This is a function that renders a HTML template when a numeric parameter
    is passed to the /number_template route
    """
    return launch("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def n_route_odd_even(n):
    """
    This is a function that renders a HTML template when a numeric parameter
    is passed to the /number_odd_or_even route and returns if the number is
    an odd number or even number
    """
    return launch("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
