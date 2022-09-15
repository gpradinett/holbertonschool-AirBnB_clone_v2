#!/usr/bin/python3
"""
sript that starts a Flask web application:
"""
from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<state_id>", strict_slashes=False)
def states(state_id=None):
    """
    function that returns states
    """
    if state_id is None:
        states = storage.all("State")

    else:
        states = storage.all("State")
        state_id = "State." + state_id

    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    function that returns a states list
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
