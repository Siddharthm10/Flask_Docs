# flask-wtf
Usually, people write forms in html. But we can also write forms directly in python using some predefined classes. 

### Features:
- Integration with WTForms.
- Secure Form with CSRF token.
- Global CSRF protection.
- reCAPTCHA support.
- File upload that works with Flask-Uploads.
- Internationalization using Flask-Babel.


### Terminology required :
1. Validators: These are restrictions and checks on the inputs taken in the forms. For example: <br>
   1. DataRequired() -> Data is required and cannot be left empty.<br>
   2. Email() -> Data input to this feild should be an emailid.<br>
   3. EqualTo("NAME") -> Check the value of the feild named "NAME".<br>
   4. Length(min=2, max=20) -> input length should be between (2,20).<br>
   Thus there are many validators which we can use to customize our forms input values.<br>

2. InputType Class: These are predefined input classes that are defined in WTForms. For example:<br>
    1. StringField -> Normal String fields.<br>
    2. BooleanField -> Boolean True/False values.<br>
    3. SubmitField -> Submit Button.<br>
    4. PasswordField -> For password.<br>
    5. FileField -> Supports uploading files.<br>
    6. FileAllowed -> Helps us defining the allowed file extensions.<br>
    Thus there are many such input types which we can use in our forms.<br>

### How to use WTForms:
Step 1: Define form types:<br>
 - In our example we have used, Registration and login forms. You can see how they are to be defined [here](example_app/forms.py).<br>
  - Once these classes are defined we can create any number of instances of these forms on our website/webapp.<br>
```
class RegistrationForm(FlaskForm):
    username = StringField("Username",
                            validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField("Email",
                        validators=[DataRequired(), Email()])

    password = PasswordField('Password', 
                            validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password',
                          validators=[DataRequired(), EqualTo("Password")])

    submit = SubmitField("Sign Up")
```

Step 2: Import the classes to the app:
  - Import all the required form types that we defined to the [app.py](example_app/app.py) file. (as done on line 2)<br>
```
from forms import RegistrationForm
```

Step 3: Create an instance and pass it into the html template.[Example](example_app/templates/register.html)<br>
- define method to the html form tag.<br>
- form.hidden_tag() -> creates a csrf token for added security to the form value.<br>
- form.username.label() -> accesses the username variable of the registration form that we created. (inside the paranthesis we can give classes for added styling.)<br>
- form.username.errors -> When the validators find any type of errors they return it in this variable. We can loop through errors in all the fields to show the list of errors or checks to correct while filling the form next time.<br>

```
form = RegistrationForm()
```

Step 4: Add a route to the main app.py file where you want to use this form:<br>
- Create an instance of form and save it in a variable<br>
- Call form.validate_on_submit() -> for the validators to check the input for any errors.<br>
  
```
@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        redirect(url_for("home"))
    return render_template('register.html', title='Register', form=form)
```

Following this steps you can easily create any type of form in python using WTForms.<br>
