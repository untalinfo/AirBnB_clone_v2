#!/usr/bin/python3
"""start flask and set a route"""

from flask import Flask, render_template
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Closes sessions"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb(id=None):
    """
    Returns the page of Airbnb
    """
    return render_template(
        '100-hbnb.html',
        states=storage.all(State).values(),
        amenities=storage.all(Amenity).values(),
        places=storage.all(Place).values()
    )



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
