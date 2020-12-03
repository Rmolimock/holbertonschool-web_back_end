#!/usr/bin/env python3
""" flask babel """

from flask import Flask, render_template
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
    if not user:
        return request.accept_languages.best_match(app.config_class.LANGUAGES)
    return user.locale


@app.route('/', methods=["GET"], strict_slashes=False)
def index():
    """ simplest route """
    return render_template('1-index.html')


if __name__ == "__main__":
    """ entry point """
    app.run(host="0.0.0.0", port="5000")
