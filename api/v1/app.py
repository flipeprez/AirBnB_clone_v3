#!/usr/bin/python3
"""Status of your API"""
from api.v1.views import app_views
from models import storage
from flask import Flask, jsonify
import os


app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def close(a):
    """Handle the app.teardown_appcontext"""
    return storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """Message error 404"""
    response = jsonify({"error": "Not found"})
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST'),
            port=os.getenv('HBNB_API_PORT'), threaded=True)
