from flask import Flask, render_template, request, redirect, url_for
from models.models import db
from services.services import PostService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wordpress.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    posts = PostService.get_all_posts()
    return render_template('index.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        PostService.create_post(
            title=request.form['title'],
            content=request.form['content'],
            author=request.form['author']
        )
        return redirect(url_for('index'))
    return render_template('post_form.html', title="Створити новину")

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    post = PostService.get_post_by_id(id)
    if request.method == 'POST':
        PostService.update_post(
            id,
            title=request.form['title'],
            content=request.form['content'],
            author=request.form['author']
        )
        return redirect(url_for('index'))
    return render_template('post_form.html', post=post, title="Редагувати")

@app.route('/delete/<int:id>')
def delete(id):
    PostService.delete_post(id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)