# Blueprints
A blueprint defines a collection of views, templates, static files and other elements that can be applied to an application.The killer use-case for blueprints is to organize our application into distinct components. 

### How to use? 
Step 1: Plan things out.
    1. If you are creating a new website or chaging the structure of the webapp using Blueprints, plan out everything.
    2. Things like number of different blueprints required, different features.

Step 2: Make new Directories for those features/group of routes:
    1. Create seperate files for each category.
    2. Files to be created depend on your webapp.
For the example we are considering the files to be created are:
- \_\_init__.py : for treating the category as a package
- routes.py : for the category related routes
- utils : for the functions used in the routes.

Step 3: After the files have been created, import Blueprints and initiate the blueprint
```
from flask import Blueprints

users = Blueprint("users", __name__)
```

Step 4: Now instead of using app.routes() (which we would normally do), we should use users.routes() (Here is an example route):
```
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))
```

Step 5: Register the blueprints in applications main \_\_init__.py file:<br>
You will have to import the blueprint from the *application.category* and the register it.
```
from app.users.routes import users
app.register_blueprint(users)
```

Step 6: Now that the blueprints are registered, you can easily develop the routes and function accordingly in those specific files.

**NOTE**: If you already were working with a webapp and are working to restructure the app with blueprints.<br>
Remember changing the following things:
  - For every use of `url_for('/route')` change it to `url_for('/category.route')` : So that the route is found in the specific category package.
  

More features and uses regarding to flask Blueprints will be added here as I come accross them.<br>

---

### Your contributions are always welcomed

