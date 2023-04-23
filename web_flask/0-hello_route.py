#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application
=======
"""Starts a Flask web application.
>>>>>>> 4ca6db531cf0ed6626b6f5e8f3782ab41b8ca898
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
<<<<<<< HEAD
    return "Hello HBNB!"


if __name__ == '__main__':
=======
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
>>>>>>> 4ca6db531cf0ed6626b6f5e8f3782ab41b8ca898
    app.run(host="0.0.0.0")
