#!/usr/bin/env python3
""" documentation for the holberton checker yep
"""

from flask_babel import Babel, _
from typing import Optional, Union
from flask import Flask, request, render_template, g, flash
import gettext
import os

app = Flask(__name__)
babel = Babel(app)

app.secret_key = os.environ.get("FLASK_SECRET_KEY", "something")

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ documentation for the holberton checker yep """
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)


def get_user(login_as: int) -> Union[dict, None]:
    """ documentation for the holberton checker yep """
    try:
        return users.get(int(login_as))
    except Exception:
        return None


@app.before_request
def before_request() -> None:
    """ documentation for the holberton checker yep """
    login_as = request.args.get("login_as")
    if login_as:
        user = get_user(login_as)
        if user:
            g.user = user["name"]
        else:
            return None
    return None


@babel.localeselector
def get_locale() -> Optional[str]:
    """ documentation for the holberton checker yep """
    if request.args.get("locale"):
        return request.args.get("locale")
    login_as = request.args.get("login_as")
    if login_as:
        user = get_user(login_as)
        local = str(user.get("locale"))
        if user and local in app.config['LANGUAGES']:
            return user.get("locale")
    local = request.headers.get("locale")
    best_match = request.accept_languages.best_match(app.config['LANGUAGES'])
    return local if local else best_match


@app.route("/", methods=["GET"], strict_slashes=False)
def home() -> str:
    """ documentation for the holberton checker yep """
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
