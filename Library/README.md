
# What are the basic commands to create a django project?

To start a django project, open the terminal on the destination directory and run:

django-admin startproject locallibrary
After running the command above, it's recommendend to change the terminal to the application's folder.

cd locallibrary

## How should it be structured? 

Initially:

locallibrary/         # Website folder
    manage.py         # Script to run Django tools for this project (created using django-admin)
    locallibrary/     # Website/project folder (created using django-admin)
    catalog/          # Application folder (created using manage.py)


Catalog folder is created by running the following command after creating a django project:

```

# Linux/macOS
python3 manage.py startapp catalog

# Windows
py manage.py startapp catalog

```

After running the command to create the catalog or any other folder the structure will be:

locallibrary/
    manage.py
    locallibrary/
        __init__.py
        settings.py
        urls.py
        wsgi.py
        asgi.py

# Updating the project 

Remember to update the project's configuration on settings.py and urls.py
It's important to first add the catalog on the application list and the database in settings.py.


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='catalog/')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


After creating models or modifying the project, it is necessary to update the project by running the following commands on the terminal: 

```
python3 manage.py makemigrations
python3 manage.py migrate
```


# Running the server

```
python3 manage.py runserver
```server

# admin.py

For educational purposes only I create a user called paganini with the password DjangoDev, it is critical to think about security, this is not a good pratice, repositories can be a great source for private passwords.

Nonetheless views must be registered on the admin.py. To create an user go to the manage.py folder and execute the following command.

```
python3 manage.py createsuperuser
``` 

After a superuser is created is possible to use the djano admin site on http://127.0.0.1:8000/admin . Django's admin site is useful to test the models. It's important that the models are registed beforehand on (/django-locallibrary-tutorial/catalog/admin.py)

The Django admin application can use your models to automatically build a site area that you can use to create, view, update, and delete records