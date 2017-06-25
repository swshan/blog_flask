#coding=utf-8

import json

from blog.models.db import session, Post

from flask import  Blueprint, render_template, request, jsonify, url_for, redirect
from sqlalchemy.sql import select



bp_views = Blueprint('views', __name__, url_prefix="")

'''
def jsonify(**kwwargs):
    response = make_response(json.dumps(kwargs))
    response.header['Content-Type'] = 'application/json; charset=utf-8'
    response.last_modified = 
'''

def cache_header():
    ''' todo header cache function '''
    pass


@bp_views.route('/api/v1/posts/get', methods=['GET'])
def index():
    posts = session.query(Post).all()
    session.close()

    posts_list = [post.to_json() for post in posts]
    print jsonify(result=posts_list)
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
            try:
                session.commit()
            except:
                session.rollback()
            source = "123"
            return redirect('/admin/add/<string:source>', source)
    else:
        args = request.args
        page = args.get('page', 1)
        page = int(page)
        offset = (page - 1)*10
        entries = session.query(Post).offset(offset).limit(10).all()     
        mydict = {
                  'key1': 'value1' 
                 }
        return render_template("add.html", entries=entries, mydict = mydict)

@bp_views.route('/api/v1/post/delete/<int:post_id>', methods=['POST'])
def post_delete(post_id):
    post = session.query(Post).filter(Post.post_id == post_id)
    if post:
        post.delete()
        session.commit()
    
    return jsonify(result="done")
