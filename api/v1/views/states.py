#!/usr/bin/python3
'''a nice comment'''
from api.v1.views import app_views
from flask import Flask, jsonify, request, abort
from models import storage
from models import State


@app_views.route('/states', strict_slashes=False)
def state():
    '''a nice comment'''
    if request.method == 'GET':
        ls = []
        for obj in storage.all(State).values():
            ls.append(obj.to_dict())
        return jsonify(ls)


@app_views.route('/states/<states_id>', methods=['DELETE'], strict_slashes=False)
def del_states(s_id):
    '''a nice comment'''
    gtstates = storage.get("states", s_id)
    if gtstates is None:
        abort(404)
    storage.delete(gtstates)
    storage.save()
    jsonify({})

@app_views.route('/states', methods=['POST'], strict_slashes=False)
def state_pos():

    gtcon = request.get_json()
    if gtcon is None:
        return (jsonify({"error": "Not a JSON"}), 400)
    name = gtcon.get("name")
    if name is None:
        return(jsonify({"error": "Missing name"}), 400)

    n_state = state(**gtcon)
    n_state.save()

    return (jsonify(n_state.to_dict()), 201)

@app_views.route('/states/<states_id>', methods=['PUT'], strict_slashes=False)
def update_states(states_id)
    '''a nice comment'''
    gtcont = request.get_json()
    if gtcont is None:
        return (jsonify({"error": "Not a JSON"}), 400)

    upstate = storage.get("state, state_id")
    if upstate is None:
        abort(404)

    n_allowed = ["id", "created_at", "updated_at"]
    for key, value in gtcont.items():
        if key not in n_allowed:
           setattr(upstate, key, value)
        upstate.save()
        return jsonify(upstate.to_dict())
