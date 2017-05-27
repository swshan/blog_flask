#coding=utf-8

import json

from blog.db import *

from flask import  Blueprint,render_template, request, jsonify
from sqlalchemy.sql import select



bp_views = Blueprint('views', __name__, url_prefix="")


@bp_views.route('/api/v1/posts/get', methods=['GET'])
def index():
    posts = session.query(Post).all()

    posts_list = [post.to_json() for post in posts]
    return jsonify(result=posts_list)


@bp_views.route('/admin/add', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if request.form['body']:
            post_title = request.form.get('title')
            post_body = request.form.get('body')
            post_category = request.form.get('category', "untag")
             
            new_post = Post(title=post_title, body=post_body,  \
                    category=post_category, pub_date=None)
            session.add(new_post)
            session.commit()
            return 'OK'
    else:
        args = request.args
        page = args.get('page', 1)
        page = int(page)
        offset = (page - 1)*10
        entries=session.query(Post).offset(offset).limit(10).all()     
        return render_template("add.html",entries=entries)

@bp_views.route('/api/v1/post/delete/<int:post_id>', methods=['POST'])
def post_delete(post_id):
    post = Post.query.get(post_id)
    if post:
        db.session.delete(post)
        db.session.commit()
    
    return jsonify(result="done")
