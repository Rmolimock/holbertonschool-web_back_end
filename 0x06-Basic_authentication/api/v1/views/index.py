#!/usr/bin/env python3
""" index routes"""

from api.v1.views import app_views
from flask import jsonify, abort


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ get status of api
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ get stats
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized() -> str:
    """ unauthorized
    """
    abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden() -> str:
    """ forbidden
    """
    abort(403)
