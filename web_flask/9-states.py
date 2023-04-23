#!/usr/bin/python3
<<<<<<< HEAD
"""Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
    /states_list: display a HTML page: (inside the tag BODY)
        H1 tag: “States”
        UL tag: with the list of all State objects present in
            DBStorage sorted by name (A->Z) tip
        LI tag: description of one State: <state.id>: <B><state.name></B>
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.place import Place
=======
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.
"""
from models import storage
from flask import Flask
from flask import render_template
>>>>>>> 4ca6db531cf0ed6626b6f5e8f3782ab41b8ca898

app = Flask(__name__)


<<<<<<< HEAD
@app.teardown_appcontext
def teardown_db(execption):
    """Closes the database"""
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_list(id=""):
    """display a HTML page: (inside the tag BODY)
    if flag is 1 states and 0 cities
    """
    flag = 1
    states_cities = sorted(storage.all(State).values(), key=lambda d: d.name)
    if id != "":
        for state in states_cities:
            if state.id == id:
                states_cities = state
                states_cities.cities = sorted(
                    state.cities, key=lambda d: d.name)
                flag = 0
        if flag == 1:
            flag = -1
    return render_template('9-states.html', states=states_cities, flag=flag)


if __name__ == '__main__':
=======
@app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML page with a list of all States.
    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
>>>>>>> 4ca6db531cf0ed6626b6f5e8f3782ab41b8ca898
    app.run(host="0.0.0.0")
