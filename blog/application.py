#coding=utf-8
import os

from flask import Flask
from blog.views.views import bp_views
from blog.configs import settings
from flask_session import Session as SESSION

#vars
basedir = os.path.abspath(os.path.dirname(__file__))


def create_app(debug=settings.DEBUG):
    app = Flask(__name__)

    app.register_blueprint(bp_views)
    app.debug = debug

    with app.app_context():
        # Extensions like Flask-SQLAlchemy now know what the "current" app
        # is while within this block. Therefore, you can now run........
        pass

    if not app.debug:
        import logging
        from logging.handlers import SMTPHandler
        args = (('smtp.126.com', 25), 'swcmail001@126.com',['swcmail001@126.com'],\
          'app warning')
        mail_handler = SMTPHandler(args)
        mail_handler.setLevel(logging.ERROR)
        mail_handler.addHandler(mail_handler)
    return app

app = create_app(settings.DEBUG)


if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SECRET_KEY'] = settings.SECRET_KEY
    sess = SESSION()
    SESSION_TYPE = 'redis'
    sess.init_app(app)
    app.run(host='127.0.0.1', port=5002) 
