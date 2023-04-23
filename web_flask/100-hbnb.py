#!/usr/bin/python3
<<<<<<< HEAD
"""Write a script that starts a Flask web application:
    Your web application must be listening on 0.0.0.0, port 5000
    You must use storage for fetching data from the storage
        engine (FileStorage or DBStorage) =>
        from models import storage and storage.all(...)
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
=======
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /hbnb: HBnB home page.
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


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return render_template(
        "100-hbnb.html",
        amenities=sorted(storage.all(Amenity).values(), key=lambda d: d.name),
        cities=sorted(storage.all(City).values(), key=lambda d: d.name),
        places=sorted(storage.all(Place).values(), key=lambda d: d.name),
        states=sorted(storage.all(State).values(), key=lambda d: d.name),
    )


if __name__ == '__main__':
=======
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays the main HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
>>>>>>> 4ca6db531cf0ed6626b6f5e8f3782ab41b8ca898
    app.run(host="0.0.0.0")
