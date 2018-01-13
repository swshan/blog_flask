# coding=utf-8

from peewee import *


psql_db = PostgresqlDatabase('testdb', user='dbuser')

class User(Model):
    user_id = IntegerField()
    user_name = CharField()
    password = CharField()
    email = CharField()

    class Meta:
        database = psql_db

class Post(Model):
    post_id = IntegerField()
    post_user_id = IntegerField()
    post_category_id = IntegerField()
    title = CharField()
    post_body = TextField()
    post_pubdate = DateTimeField()
    is_display = BooleanField()
	
    class Meta:
        database = psql_db

class Category(Model):
    category_id = IntegerField()
    category_name = CharField()

    class Meta:
        database = psql_db


psql_db.create_tables([User, Post, Category])
