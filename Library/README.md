
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




