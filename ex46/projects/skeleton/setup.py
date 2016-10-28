#! /usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'jianjiang'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Test Project of Jiangjian',
    'author': 'jiangjian',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'jiangjian*****@163.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
