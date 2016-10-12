#!/usr/bin/env python
"""

Getter Setter Generator

Sam Zielke-Ryner (samzielkeryner@gmail.com)

"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'description': 'Getter Setter Generator',
    'author': 'Sam Zielke-Ryner',
    'url': 'https://github.com/sqzr1',
    'download_url': 'https://github.com/sqzr1',
    'author_email': 'samzielkeryner@gmail.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['gsg'],
    'scripts': [],
    'name': 'Getter-Setter-Generator'
}


setup(**config)
