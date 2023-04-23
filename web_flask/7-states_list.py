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
=======
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
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


@app.route("/states_list", strict_slashes=False)
def states_list():
    """display a HTML page: (inside the tag BODY)"""
    return render_template(
        '7-states_list.html',
        states=sorted(storage.all(State).values(), key=lambda d: d.name)
    )


if __name__ == '__main__':
=======
@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage.
    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
>>>>>>> 4ca6db531cf0ed6626b6f5e8f3782ab41b8ca898
    app.run(host="0.0.0.0")
