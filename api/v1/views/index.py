#!/usr/bin/python3
"""Modulo index"""
from api.v1.views import app_views
import json



@app_views.route('/status')
def dict_json():
    """return json"""
    my_dict = {
        "status": "ok"
    }
    return json.dumps(my_dict)
