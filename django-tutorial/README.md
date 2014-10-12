Django Tutorial
===============

Original django tutorial

INSTALLATION
============
- Create a new project (e.g. django-admin.py startproject tutorial)
- Change the database settings, such as name and database engine in settings.py
- Create the database tables (e.g. python manage.py migrate)
- Run the development server (e.g. python manage.py runserver)
- Create a polls app (e.g. python manage.py startapp polls)
- Add the Question/Choice models to models.py (polls app)
- Add the polls app in the main settings as INSTALLED_APP
- Run makemigrations for the polls app (python manage.py makemigrations polls)
- Run migrate to create the tables for the previously created models
- Create a super user (python manage.py createsuperuser)

SOURCE
=============
- [Part I](http://goo.gl/SzSReE)
- [Part II](http://goo.gl/SiIPIK)
- [Part III](http://goo.gl/002Y3o)
- [Part IV](http://goo.gl/Gd7nm4)
- [Part V](http://goo.gl/6OEAcc)
- [Part VI](http://goo.gl/a3JMkT)