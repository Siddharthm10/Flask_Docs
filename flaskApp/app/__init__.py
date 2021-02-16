# the folder should be the same name as app
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config["SECRET_KEY"] = 'e26c68370f78f595cc3508249f91df41'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #Database path
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get("EMAIL_USER")
app.config['MAIL_PASSWORd'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)
#initiating the database
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
#if a decorator with login fails this is the route where the function is redirected
login_manager.login_message_category = 'info' # this is for styling the flashed message


from app import routes