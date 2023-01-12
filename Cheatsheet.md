# Start project
- Create project folder
- Create virtual environment:
```py
    virtualenv env
    source env/bin/activate
```
- Install Django or Django Rest Framework
```py
pip install djangorestframework
```
- Create requirements.txt same level with working directory, send your installed packages to this file, requirements file must be up to date:
```py
pip freeze > requirements.txt
```
- Create project (with . it creates a single project folder avoiding nested folders)
```py
django-admin startproject main .
```
- Add 'rest_framework' to your INSTALLED_APPS in settings.py. Always add new apps to settings.py!
```py
INSTALLED_APPS = [
    # ...
    # Third party apps:
    'rest_framework',

    # My apps:
]
```
- Add .gitignore file to root
- To use python decouple in this project, first install it:
```py
pip install python-decouple
```

- Update requirements.txt:
```py
pip freeze > requirements.txt
```

- For more information look at [python-decouple documentation](https://pypi.org/project/python-decouple/)

- Import the config object on settings.py file:
```py
from decouple import config
```

- Create .env file on root directory. We will collect our variables in this file.
```py
SECRET_KEY=t5o9...
```

- You can use [django secret key generator apps](https://djecrety.ir/)

- Retrieve the configuration parameters in settings.py:
```py
SECRET_KEY = config('SECRET_KEY')
```

- Push code to Github and commit after each step

- Create a new application (Don't forget to add it to settings.py!)
```py
python manage.py startapp <app name>
```

# Create models
- Create your models

- Create tables and apply them to the db:
```py
python manage.py makemigrations
python manage.py migrate
```
- Repeat above steps after any changes in your database tables
- `makemigrations` creates tables from models, whereas `migrate` sends tables to the database

- Register models to admin dashboard:
```py
from .models import Passenger, Flight, Reservation

admin.site.register(Passenger)
admin.site.register(Flight)
admin.site.register(Reservation)
```

- Create superuser
```py
python manage.py createsuperuser
```

# Create serializers
- Create a new serializers.py file in the app folder

# Create views
- Choose one view class: generic views, functional views or viewsets

# Create URLs
- Create a new file `app/urls.py` in the app folder
- Include app/urls.py to main url patterns
```py
path('app/', include('app.urls')),
```
- import `include`in main/urls.py
- Use this code for class-based views
```py
path('cars/', CarListView.as_view()),
```

- Create URL patterns / paths

# Testing with Postman

# Permissions
- Choose a permission class
- If none of the classes fits your needs, create a custom permission class
- Create app/permissions.py and a custom permission class OR add built-in authentication to a class-based view
- For function-based views you must use related decorators
- Import custom classes in views.py to use them

# Authentication
- Choose between basic, token or session authentication
- Add dj_rest_auth app to INSTALLED_APPS in your django settings:

### Setting the authentication scheme

The default authentication schemes may be set globally, using the DEFAULT_AUTHENTICATION_CLASSES setting. We will use token auth.

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```

## Install dj-rest-auth

In this project, we will use dj-rest-auth. Follow [documentation](https://dj-rest-auth.readthedocs.io/en/latest/installation.html) and install.

- Install package:
```py
pip install dj-rest-auth
```

- Update requirements.txt:
```py
pip freeze > requirements.txt
```

- Add dj_rest_auth app to INSTALLED_APPS in your django settings:
```py
'rest_framework.authtoken',
'dj_rest_auth',
```

- Migrate your database, this will apply db tables originated from auth token:
```py
python manage.py migrate
```

- Include users.urls to main url pattern. Create users/urls.py and add dj_rest_auth:
```py
urlpatterns = [
    path('dj-rest-auth/', include('dj_rest_auth.urls'))
]
```

- Check the endpoints;
  - Login (See the token created by package)
  - Logout
 

# Spinning up an existing project
- Clone project from Github
- Create virtual environment and activate it
- Install dependencies:
```py
pip install -r requirements.txt
```