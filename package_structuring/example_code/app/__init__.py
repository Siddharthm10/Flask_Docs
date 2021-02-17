# the folder should be the same name as app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = 'e26c68370f78f595cc3508249f91df41'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #Database path
#initiating the database
db = SQLAlchemy(app)

from app import routes