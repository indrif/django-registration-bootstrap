Django Registration Bootstrap
=============================

Install it
----------

.. code-block:: bash

    $ pip install https://github.com/indrif/django-registration-bootstrap/archive/master.zip

Into the settings file, add the following to ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = (
        # ... everything else

        # Add the templates via INSTALLED_APPS
        'registration_bootstrap3',
    )





Simple sample using bootstrap from twitter in forms of Django
-------------------------------------------------------------

Using Bootstrap from Twitter version 3.3.5

And Django version 1.8

http://twitter.github.com/bootstrap

To run, just download and do runserver:
``shell     python manage.py runserver 8000``

username: demo password: demo

Screenshots
===========

For screenshots, check original repo: https://github.com/ebertti/django-registration-bootstrap

Changelog
---------

2015-11-10 by indrif

- Update to Bootstrap 3.5.3 and Django 1.8

2014-01-16 by EBertti

-  Update Bootstrat to 3.0.3 and Django to 1.6.1
