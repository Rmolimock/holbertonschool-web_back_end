#!/usr/bin/env python3
""" flask babel """

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ Configuring Babel """
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)


def get_user(user_id):
    """ get user """
    if not user_id:
        return None
    user_id = int(user_id)
    if not user_id in users:
        return None
    return users[user_id]


@app.before_request
def before_request():
    """ before """
    g.user = get_user(request.args.get('login_as'))


@babel.localeselector
def get_locale():
    """
    get local language code
    """
    user = getattr(g, 'user', None)
    if user:
        return user.locale
    lan = request.args.get('locale')
    if lan:
        if lan in app.config['LANGUAGES']:
            return lan
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=["GET"], strict_slashes=False)
def index():
    """ simplest route """
    return render_template('1-index.html')


if __name__ == "__main__":
    """ entry point """
    app.run(host="0.0.0.0", port="5000")
