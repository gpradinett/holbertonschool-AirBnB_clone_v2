#!/usr/bin/python3
"""
sript that starts a Flask web application:
"""
from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    function that returns states
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")

    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    function that returns a states list
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
