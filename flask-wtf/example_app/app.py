from flask import Flask, render_template, url_for, flash,redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = 'e26c68370f78f595cc3508249f91df41'


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
    return render_template('home.html', posts=posts )


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        redirect(url_for("home"))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@blog.com' and form.password.data == 'password':
            flash("You have been logged in !", "success")
            return redirect(url_for("home"))
        else:
            flash("login unsuccessful. Please Check username and password.", "danger")
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)