from PIL import Image
import os
import secrets
from flask_mail import Message
from flask import current_app
from app import mail

def save_picture(form_picture):
    # randomize the name of the image
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, "static/profile_pics", picture_fn)
    
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn



def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                 sender='noreply@demo.com',
                 recipients=[user.email])
    # _external is to get the external url and not the relative user
    msg.body = ''' To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be done.
    '''
    mail.send(msg)
