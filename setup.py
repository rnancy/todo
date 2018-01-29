#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


version = '0.0.2'

description = '''Tools to manage Todos'''
long_description = '''application to manage your todo list'''

url = 'https://github.com/rnancy/todo'
download_url = 'https://github.com/rnancy/todo/archive/%s.tar.gz'

setup(
    name='pytodo',
    version=version,
    description=description,
    long_description=long_description,
    author='Rose Nancy',
    url=url,
    download_url=download_url % version,
    packages=find_packages(),
    install_requires=[
        'setuptools',
        'PTable==0.9.2',
        'argparse',
        'SQLAlchemy==1.1',
    ],
    tests_require=[
    ],
    test_suite='',
    entry_points={
        'console_scripts': [
            'todo.add_project = pytodo.apps.add_project:main',
            'todo.add_task = pytodo.apps.add_task:main',
            'todo.add = pytodo.apps.add:main',
            'todo.list = pytodo.apps.list:main',
            'todo.delete = pytodo.apps.delete:main',
        ],
    },
    extras_require={
#        'postgres':  ['psycopg2'],
    },
)
