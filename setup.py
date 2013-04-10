#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'django-dbdump',
    version = '1.0',
    url = 'https://github.com/vitaliyf/django-dbdump/',
    download_url = 'https://github.com/vitaliyf/django-dbdump/',
    license = 'BSD',
    description = 'Database backup management command.',
    long_description=read('README.rst'),
    author = 'Vitaliy Fuks',
    author_email = 'vitaliyf@gmail.com',
    packages = find_packages(),
    include_package_data = True,
    platforms='any',
    classifiers = [
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=[
        'Django>=1.2',
    ],
)
