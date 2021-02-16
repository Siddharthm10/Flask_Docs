from flask import Flask, render_template, url_for, flash,redirect
from sqlalchemy.orm import backref
from wtforms.validators import Email
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = 'e26c68370f78f595cc3508249f91df41'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #Database path
#initiating the database
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}'', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    
    def __repr__(self):
        return f"User('{self.title}'', '{self.date_posted}')"


posts = [
    {
        'author':'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20,2018'
    },
    {
        'author':'Siddharth Mehta',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'April 21,2018'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return "<h1> Home Page</h1>"
    # return render_template('home.html', posts=posts )


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        print("User added to database: {}".format(User.query.filter_by(username="Siddharth").first()))
        redirect(url_for("home"))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data, password=form.password.data).first()
        print(user, form.email.data, form.password.data)
        if user:
            flash("You have been logged in !", "success")
            print("logged in successfully")
            return redirect(url_for("home"))
        else:
            flash("login unsuccessful. Please Check username and password.", "danger")
            print("wrong credentials")
    return render_template('login.html', title='Login', form=form)

@app.route('/cleaning')
def cleaning():
    db.drop_all()
    print("database cleared")
    db.create_all()
    return "<h1> Database Cleared</h1>"

if __name__ == "__main__":
    app.run(debug=True)