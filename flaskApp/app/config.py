import os

class Config:
    SECRET_KEY = 'e26c68370f78f595cc3508249f91df41'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' #Database path
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORd = os.environ.get('EMAIL_PASS')
