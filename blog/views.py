#coding=utf-8

import json

from blog.db import *

from flask import  Blueprint,render_template, request, jsonify


bp_views = Blueprint('views', __name__, url_prefix="")


@bp_views.route('/api/v1/posts/get', methods=['GET'])
def index():
    posts = Post.query.all()

    posts_list = [post.to_json() for post in posts]
    return jsonify(result=posts_list)


@bp_views.route('/admin/add', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if request.form['body']:
            post_title = request.form.get('title')
            post_body = request.form.get('body')
            post_category = request.form.get('category', "untag")
             
            new_post = Post(post_title, post_body,  \
                    post_category)
            db.session.add(new_post)
            db.session.commit()
            return 'OK'
    else:
        args = request.args
        entries=Post.query.limit(10).all()        
        return render_template("add.html",entries=entries)

@bp_views.route('/api/v1/post/delete/<int:post_id>', methods=['POST'])
def post_delete(post_id):
    post = Post.query.get(post_id)
    if post:
        db.session.delete(post)
        db.session.commit()
    
    return jsonify(result="done")
