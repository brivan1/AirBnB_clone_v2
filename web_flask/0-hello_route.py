#!/usr/bin/python3
"""
A Python Flask script that starts a web application 
and listens on port 5000 with ip 0.0.0.0
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Function that returns “Hello HBNB!” from the root route
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
