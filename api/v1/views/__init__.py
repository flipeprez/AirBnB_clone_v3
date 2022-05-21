#!/usr/bin/python3
"""modulo Blueprint"""
from flask import Blueprint
from api.v1.views.index import *


app_views = Blueprint('app_views', __name__)
