# flask-mail
Flask Mail is used to add the mail sending functionality to the webapps that you use.

It uses SMTP functionality in the backend.

### How to use?
Step 1: Import flask_mail<br>
```from flask_mail import Mail```

Step 2: Set some configurations(Here are some for gmail):<br>
```
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get("EMAIL_USER")
app.config['MAIL_PASSWORd'] = os.environ.get('EMAIL_PASS')
```
**Note**: Enter your own mail and password in the last two lines.

Step 3: Set message<br>
```
from flask_mail import Message
msg = Message('Password Reset Request',
                 sender='noreply@demo.com',
                 recipients=[user.email])
# _external is to get the external url and not the relative user
msg.body = "Message"
mail.send(msg)
```
Thus mail is sent to the user.

For more functionalities like adding an attachment etc. you can check out the official documentations for flask-mail.
