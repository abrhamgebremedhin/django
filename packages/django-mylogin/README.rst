=====
Mylogin
=====

Mylogin is a simple Django app 
 

Quick start
-----------

1. Add "Mylogin" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'Mylogin',
    ]

2. Include the Mylogin URLconf in your project urls.py like this::

    path('Mylogin/', include('Mylogin.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/Mylogin/ 
 
5. Add this to the settings.py of the project

		#core-app settings 

		LOGIN_REDIRECT_URL = 'home'
		LOGOUT_REDIRECT_URL = 'home'

6. Change 'DIRS' under TEMPLATES in settings.py of the project to

		'DIRS': [os.path.join(BASE_DIR,"templates")],

7. You are ready to go
