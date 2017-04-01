import db

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if request.form['body']:
            post_title = request.form.get['title','null']
            post_body = request.form.get['body', 'null']
            post_pub_date = request.form.get['pub_date', 'null']
            post_category = request.form.get['category', 'null']
            new_post = Post(post_title, post_body, post_pub_date,  \
                    post_category)
            db.session.add(new_post)
            db.session.commit()

    
    else:
        args = request.args

        render_template()

if __name__ == '__main__':
    app.run()
