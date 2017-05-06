
from db import * 

import json

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)



@app.route('/api/v1/posts/get')
def index():
    posts = Post.query.all()
    posts_list = [post.to_json() for post in posts]
    return jsonify(result=posts_list)


@app.route('/admin/add', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if request.form['body']:
            post_title = request.form.get('title')
            post_body = request.form.get('body')
            post_category = request.form.get('category', "untag")
            print post_title
            new_post = Post(post_title, post_body,  \
                    post_category)
            db.session.add(new_post)
            db.session.commit()
            return 'OK'
    else:
        args = request.args
        entries=Post.query.limit(10).all()        
        return render_template("add.html",entries=entries)


if __name__ == '__main__':
    app.run(debug=True)
