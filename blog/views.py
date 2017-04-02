from db import * 

from flask import Flask, render_template, request

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)



@app.route('/')
def index():
    return render_template('index.html')

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
            return 'OK'
    else:
        args = request.args
        entries=Post.query.limit(10).all()        
        return render_template("add.html",entries=entries)

if __name__ == '__main__':
    app.run(debug=True)
