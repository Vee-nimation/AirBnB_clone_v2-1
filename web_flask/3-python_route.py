#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space )
    /python/(<text>): display “Python ”, followed by the value of
        the text variable
=======
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
>>>>>>> 4ca6db531cf0ed6626b6f5e8f3782ab41b8ca898
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
<<<<<<< HEAD
    """Displays 'Hello HBNB!'"""
=======
    """Displays 'Hello HBNB!'."""
>>>>>>> 4ca6db531cf0ed6626b6f5e8f3782ab41b8ca898
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
<<<<<<< HEAD
    """Displays 'HBNB'"""
=======
    """Displays 'HBNB'."""
>>>>>>> 4ca6db531cf0ed6626b6f5e8f3782ab41b8ca898
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
<<<<<<< HEAD
def c_is_fun(text=None):
    """Displays 'C {text}'"""
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text='is_cool'):
    """Displays 'C {text}'"""
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
=======
def c(text):
    """Displays 'C' followed by the value of <text>.
    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of <text>.
    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
>>>>>>> 4ca6db531cf0ed6626b6f5e8f3782ab41b8ca898
    app.run(host="0.0.0.0")
