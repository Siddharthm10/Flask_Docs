# flask-login
Flask-Login provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time.

### Features
It will
- Store the active user’s ID in the session, and let you log them in and out easily.
- Let you restrict views to logged-in (or logged-out) users.
- Handle the normally-tricky “remember me” functionality.
- Help protect your users’ sessions from being stolen by cookie thieves.
- Possibly integrate with Flask-Principal or other authorization extensions later on.

However, it will not,
- Impose a particular database or other storage method on you. You are entirely in charge of how the user is loaded.
- Restrict you to using usernames and passwords, OpenIDs, or any other method of authenticating.
- Handle permissions beyond “logged in or not.”
- Handle user registration or account recovery.

Basically there are a lot of features required when we talk about the User Authentication and their login and logout. And flask-login has many pre-built functions and methods and decorators that we can easily help

### How to use?
Step 1: Import flask-login: <br>
``` from flask-login import LoginManager```

Step 2: Initiate an instance:
```
login_manager = LoginManager(app)
```

Step 3: Import the `login_manager` to the routes file:
```
from app import login_manager
```

Step 4: Basic & easy to use API's with their functions:
1. `login_user(user, remember=form.remember.data)` -> logins the user to the database, takes in two inputs: user(database element), remember me(selection to stay logged in.)
2. `logout_user()` -> logs the user out from the website.
3. `current_user` -> Its the details regarding the currently logged in user.(current_user.is_authenticated -> returns if the user is already logged in)
4. `login_required` -> This is a decorator and can be used for the pages which required user to be logged in.


Step 5: You can use the above functionalities to cutomize the fuctions according to your will.
```
@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.email.data).first()
        passwordCheck = bcrypt.check_password_hash(user.password, form.password.data)
        if user and passwordCheck:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("Login unsuccessful. Please check email and password.", "danger")
            print("wrong credentials")

    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required #cant access the page without loggin in
def account():
    return render_template('account.html', title='Account')
```


This is how you can use flask-login functionality.
