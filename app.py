from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    hobby = db.Column(db.String(100))
    age = db.Column(db.Integer)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods=['POST'])
def add_user():
    username = request.form['username']
    hobby = request.form['hobby']
    age = request.form.get('age', 0)
    new_user = User(username=username, hobby=hobby, age=int((age)))
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('list_users'))

@app.route('/users')
def list_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/remove', methods=['POST'])
def delete_users():
    # username = request.form['username']
    # rem_user = User.query.filter_by(username=username).first()
    user_id = request.form['id']
    user = User.query.get(user_id)
    # if rem_user:
    if user:
        # db.session.delete(rem_user)
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('list_users'))

@app.route('/update/<int:id>', methods=['POST'])
def update_users(id):
    # username = request.form['username']
    # new_age = request.form['age']

    # user = User.query.filter_by(username=username).first()
    # if user:
    #     user.age = int(new_age)
    #     db.session.commit()
    user = User.query.get(id)
    if user:
        user.username = request.form['username']
        user.age = request.form['age']
        user.hobby = request.form['hobby']
        db.session.commit()
    return redirect(url_for('list_users'))

@app.route('/edit/<int:id>', methods=['GET'])
def edit_users(id):
    user = User.query.get(id)
    return render_template('edit.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)