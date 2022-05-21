#!/usr/bin/python3
"""Modulo index"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def dict_json():
    """return json"""
    my_dict = {
        "status": "OK"
    }
    return jsonify(my_dict)
