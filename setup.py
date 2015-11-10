#!/usr/bin/env python
# -*- coding: utf-8 -*-

import registration_bootstrap3 as app

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = app.__version__

readme = open('README.rst').read()


setup(
    name='django-registration-bootstrap3',
    version=version,
    description="""Custom HTML template for django-registration app made using Bootstrap from Twitter""",
    long_description=readme,
    author=u'Ezequiel Bertti',
    author_email='ebertti@gmail.com',
    url='https://github.com/ebertti/django-registration-bootstrap',
    packages=[
        'registration_bootstrap3'
    ],
    package_data={
        'registration_bootstrap3': ['static/*/*/*', 'templates/*', 'templates/*/*', 'templatetags/*']
    },
    include_package_data=True,
    license="BSD",
    zip_safe=False,
    keywords='django registration bootstrap auth users',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
