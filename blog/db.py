# coding=utf-8
import datetime

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, MetaData
from sqlalchemy import BigInteger, DateTime, String, CHAR, Text, Integer,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

BaseModel = declarative_base()
#session_engine = create_engine('sqlite://dbuser:password@localhost:5432/mydb')

session_engine = create_engine('postgresql://dbuser:password@localhost:5432/mydb')
Session = sessionmaker(session_engine)
session = Session()

class User(BaseModel):
    __tablename__ = 'user'

    user_id = Column(CHAR(64), primary_key=True)
    name = Column(String(32), server_default='', nullable=False)
    email = Column(String(32), server_default='', nullable=False)

class Post(BaseModel):
    __tablename__ = 'post'
    
    post_id = Column(Integer, primary_key=True,autoincrement=True)
    title = Column(String(128))
    body = Column(String(2048))
    #category_id = Column()
    category = Column(Text())
    pub_date = Column(DateTime())

    def __init__(self, title, body, category, pub_date):
        self.title = title
        self.body = body
        self.category = category
        if self.pub_date is None:
            self.pub_date = datetime.date.today()
        self.pub_date = datetime.date.today()

    def to_json(self):

    	return {
    	    'pid': self.post_id,
    	    'title': self.title,
    	    'body': self.body,
            'date': pub_date,
            'category': category
    	}

class Categories(BaseModel):
    __tablename__ = 'category'

    category_id = Column(Integer, primary_key=True)
    category = Column(String(128))
    


if __name__ == '__main__':
	BaseModel.metadata.create_all(session_engine)

