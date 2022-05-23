#!/usr/bin/python3
'''a nice comment'''
from api.v1.views import app_views
from flask import Flask, jsonify, request
from models import storage
from models.state import State


@app_views.route('/states', strict_slashes=False)
def state():
    print("a")
    if request.method == 'GET':
        ls = []
        for obj in storage.all(State).values():
            ls.append(obj.to_dict())
        return jsonify(ls)


'''
    if request.method == 'POST'
	n_state = storage.new(State)
	request.get_json('n_state')
    '''
'''@app.route('/states/<states_id>', method=['GET', 'DELETE', 'PUT'], strict_slashes=False)
def state_id(state_id = None)
    if state_id is None:
	dic = {}
	raise TypeError 404
	 '''