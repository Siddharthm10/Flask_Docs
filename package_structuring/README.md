# Package Structuring
Package Structuring means distributing the entire code over various files and work with it.
### We'll take the example of this tree:
    .
    ├── app
    │   ├── forms.py
    │   ├── __init__.py
    │   ├── models.py
    │   ├── routes.py
    │   ├── site.db
    │   ├── static
    │   │   └── styles
    │   │       └── bootstrap.min.css
    │   └── templates
    │       ├── home.html
    │       ├── login.html
    │       └── register.html
    └── run.py



**Note**: This can be generated via command line:
- Go to the directory for which you want the tree.
- `sudo apt-get install tree` 
- `tree` : this give the project tree.

#### One by one we'll understand the contents of each file:
1. \_\_init__.py: This contains the initialization of the app and the database(in this example).
2. forms.py: This contains all the different types of forms that you want to use in your app.
3. models.py: This contains all the different types of database objects that you want to use in your webapp.
4. routes.py: This contains all the route functions for the app.
5. static: This contains all the assets and the styling of the app.
6. templates: This contains all the html templates that the app uses.
7. run.py: This executes the app

This is how a basic project can be structured.