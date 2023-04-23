#!/usr/bin/python3
<<<<<<< HEAD
"""starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
=======
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
>>>>>>> 4ca6db531cf0ed6626b6f5e8f3782ab41b8ca898
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
<<<<<<< HEAD
=======
    """Displays 'Hello HBNB!'."""
>>>>>>> 4ca6db531cf0ed6626b6f5e8f3782ab41b8ca898
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
<<<<<<< HEAD
    return "HBNB"


if __name__ == '__main__':
=======
    """Displays 'HBNB'."""
    return "HBNB"


if __name__ == "__main__":
>>>>>>> 4ca6db531cf0ed6626b6f5e8f3782ab41b8ca898
    app.run(host="0.0.0.0")
