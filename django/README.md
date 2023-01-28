
# Polls

Polls is a Django app to conduct Web-based polls. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation in <https://docs.djangoproject.com/es/3.0/intro/tutorial01/>

## Quick start

1. Django project, execute with
    ```python3 manage.py runserver```

2. Start the development server and visit <http://127.0.0.1:8000/admin/>
   to create a poll

3. Visit <http://127.0.0.1:8000/polls/> to access to polls module

The application has the following aspect:

```django/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
    polls/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
            0001_initial.py
        models.py
        static/
            polls/
                images/
                    background.gif
                style.css
        templates/
            polls/
                detail.html
                index.html
                results.html
        tests.py
        urls.py
        views.py
    templates/
        admin/
            base_site.html``
