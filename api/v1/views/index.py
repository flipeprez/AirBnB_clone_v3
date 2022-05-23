#!/usr/bin/python3
"""Modulo index"""
from models import storage
from models.state import State
from api.v1.views import app_views
from flask import jsonify
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User


@app_views.route('/status')
def dict_json():
    """return json"""
    my_dict = {
        "status": "OK"
    }
    return jsonify(my_dict)

@app_views.route('/stats')
def numb_obj():
    """endpoint that retrives number of each object"""
    my_dict = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }
    return jsonify(my_dict)
