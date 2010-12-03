from setuptools import setup
import os, sys

try:
    long_desc = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
except (IOError, OSError):
    long_desc = ''

dependencies = ['httplib2', 'lxml']
# add multiprocessing for Python2.4/2.5
if sys.version_info < (2, 6):
    dependencies += ['multiprocessing']

setup(
    name = "patu",
    version = '0.1',
    url = 'http://github.com/akrito/patu',
    author = 'Alex Kritikos',
    author_email = 'alex@8bitb.us',
    description = 'Patu is a small spider',
    long_description = long_desc,
    entry_points = {
        'console_scripts': ['patu = patu:main']
    },
    install_requires = dependencies,
    py_modules = ['patu'],
)
