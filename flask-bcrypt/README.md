# flask-bcrypt
Flask-Bcrypt is a Flask extension that provides bcrypt hashing utilities for your application.

Due to the recent increased prevelance of powerful hardware, such as modern GPUs, hashes have become increasingly easy to crack. A proactive solution to this is to use a hash that was designed to be “de-optimized”. Bcrypt is such a hashing facility; unlike hashing algorithms such as MD5 and SHA1, which are optimized for speed, bcrypt is intentionally structured to be slow.

### Features:
- Provides secure password hashing techniques.
- Increases app database security.

### Installation:
`pip install flask-bcrypt`

### How to use it?
Step 1: Import bcrypt
```from flask_bcrypt import Bcrypt```

Step 2: initiate an instance
``` bcrypt = Bcrypt() ```

Step 3: Generate a password hash:
``` bcrypt.generate_password_hash('testing').decode('utf-8')```
 This generates a password hash and then decodes it into utf-8 mode and returns it into a string.

 **Note**: This generates a different hash code for even the same password everytime we run this.

#### If the hashing is different everytime! How will you verify the password then?
We can save the password in a variable and then use the bcrypt.check_password_hash(variable, "userInp") method.

```
#Example
hashedPass = bcrypt.generate_password_hash('testing').decode('utf-8')
bcrypt.check_password_hash(hashedPass, "password")
```
This function returns a *boolean* and **solves** our problem.
