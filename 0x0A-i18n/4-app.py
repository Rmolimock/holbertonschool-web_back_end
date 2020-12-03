#!/usr/bin/env python3
""" flask babel """

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Configuring Babel """
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)


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
