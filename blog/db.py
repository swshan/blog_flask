
import os
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    __tablename__ = 'post'
    pid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    category = db.relationship('Category',backref="post", )    

    def __init__(self, title, body, category_id, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.category_id = category_id

    def __repr__(self):
        return '<Post %s>' % (self.title)

    def to_json(self):
        return {
            'pid': self.pid,
            'title': self.title,
            'body': self.body,
            'pub_date': self.pub_date,
        }

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return '<Category %r>' % self.name

class Session(db.Model):
    session_id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)
    expire_time = db.Column(db.DateTime)

    def __init__(self):
        pass

