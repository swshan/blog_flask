#coding=utf-8

import json

from blog.models.db import Session, Post, User, UserSession

from flask import  Blueprint, render_template, request, jsonify, url_for,  \
                     redirect, session
from sqlalchemy.sql import select


bp_views = Blueprint('views', __name__, url_prefix="")


def cache_header():
    ''' todo header cache function '''
    pass


@bp_views.route('/api/v1/posts/get', methods=['GET'])
def posts_get():
    posts = Session.query(Post).all()
    Session.close()

    posts_list = [post.to_json() for post in posts]
    print (jsonify(result=posts_list))
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
            Session.add(new_post)
            try:
                Session.commit()
            except:
                Session.rollback()
            
            return redirect('/admin/add/')
    else:
        args = request.args
        page = args.get('page', 1)
        page = int(page)
        offset = (page - 1)*10
        entries = Session.query(Post).offset(offset).limit(10).all()     

        return render_template("add.html", entries=entries)

@bp_views.route('/api/v1/post/delete/<int:post_id>', methods=['POST'])
def post_delete(post_id):
    post = Session.query(Post).filter(Post.post_id == post_id)
    if post:
        post.delete()
        session.commit()
    
    return jsonify(result="done")

@bp_views.route('/user/login/', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password is None:
            abort(400)
        user = Session.query(User).\
                         filter(User.name==username).one()
        if user is None:
            abort(400)
        session['username'] = user.name
        print ("session done")
        return redirect('/admin/add')
    else:
        return '''
            <form action="" method="post">
                <p><input type=text name="username">
                <p><input type=text name="password">
                <p><input type=submit value=Lgoin>
            </form>
          '''

@bp_views.route('/user/logout')
def logout():
    session.pop('username', None)
    print ("logout done")
    return redirect('/')

