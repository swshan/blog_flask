#coding=utf-8
import os

from flask import Flask
from blog.views.views import bp_views
from blog.configs import settings

#vars
basedir = os.path.abspath(os.path.dirname(__file__))


def create_app(debug=settings.DEBUG):
    app = Flask(__name__)
    app.register_blueprint(bp_views)
    app.debug = debug
    app.secret_key = 'Idontknowjs'

    with app.app_context():
        # Extensions like Flask-SQLAlchemy now know what the "current" app
        # is while within this block. Therefore, you can now run........
        pass

    return app

app = create_app(settings.DEBUG)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000) 
