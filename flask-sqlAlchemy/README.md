# Flask-SQLAlchemy
Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to your application. It aims to simplify using SQLAlchemy with Flask by providing useful defaults and extra helpers that make it easier to accomplish common tasks.
Here for examples we are gonna be using **sqllite** database

It uses ORM (Object Relational Mapping) to access the database from an object-oriented language.

### How to use it?

Step 1: Import the Sqlite database:<br>
``` 
from flask-sqlalchemy import SQLAlchemy
#Database path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 
db = SQLAlchemy(app)
```

Step 2: Define the Type of database classes:<br>
- As in our [example](example_app/app.py), we have created User and Post class.
- Define all the database types
  
```
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    # Magic function -> when printed creates a string for this datatype
    def __repr__(self):
        return f"User('{self.username}'', '{self.email}', '{self.image_file}')"

```

Step 3: Create a database:<br>
- Open python3 in terminal in the workspace folder:
  
```
from app import db
db.create_all()     # This creates the database file
```


Step 4: Basic Commands to work with the database:

1. `db.create_all()`: Creates all the datatypes that we have defined.
2. `User.query.all()`: Return a list of complete data.
3. `User.query.first()`: Returns the first element.
4. `User.query.filter_by(username="corey").all()`: Search for the database for a user name "corey".
5. `User.query.get(id)` : Get user by id.
6. `db.drop_all()`: Delete all data.
7. `db.session.add(user)`: Add the user to the database.
8. `db.session.commit()`: Commit the changes.


Step 5: Use the commands to use the database in your app:

```
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
```