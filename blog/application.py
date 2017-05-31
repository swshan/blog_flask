#coding=utf-8
import os

from flask import Flask
from blog.views import bp_views
from blog.db import *

#vars
basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_views)
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@127.0.0.1:3306/blog'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    with app.app_context():
        # Extensions like Flask-SQLAlchemy now know what the "current" app
        # is while within this block. Therefore, you can now run........
        pass

    return app

app = create_app()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
