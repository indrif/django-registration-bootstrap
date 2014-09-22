Django Registration Bootstrap
=============================

Install it
----------

.. code-block:: bash

    $ pip install https://github.com/ebertti/django-registration-bootstrap/archive/master.zip

Into the settings file, add the following to ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = (
        # ... everything else

        # Add the templates via INSTALLED_APPS
        'registration_bootstrap3',
    )





Simple sample using bootstrap from twitter in forms of Django
-------------------------------------------------------------

Using Bootstrap from Twitter version 3.0.3

And Django version 1.6.1

http://twitter.github.com/bootstrap

To run, just download and do runserver:
``shell     python manage.py runserver 8000``

username: demo password: demo

Screenshots
===========

.. figure:: https://raw.github.com/ebertti/django-registration-bootstrap/master/screenshot/home_pt.png
   :align: center
   :alt: home

   home
|login| |login error|

|password change| |password change error|

|password reset| |password reset error|

Changelog
---------

2014-01-16 by EBertti

-  Update Bootstrat to 3.0.3 and Django to 1.6.1

.. |login| image:: https://raw.github.com/ebertti/django-registration-bootstrap/master/screenshot/loggin_pt.png
.. |login
error| image:: https://raw.github.com/ebertti/django-registration-bootstrap/master/screenshot/loggin_error_pt.png
.. |password
change| image:: https://raw.github.com/ebertti/django-registration-bootstrap/master/screenshot/password_change_pt.png
.. |password change
error| image:: https://raw.github.com/ebertti/django-registration-bootstrap/master/screenshot/password_change_error_pt.png
.. |password
reset| image:: https://raw.github.com/ebertti/django-registration-bootstrap/master/screenshot/password_reset_pt.png
.. |password reset
error| image:: https://raw.github.com/ebertti/django-registration-bootstrap/master/screenshot/password_reset_error_pt.png
