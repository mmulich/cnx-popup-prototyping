# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
# README = open(os.path.join(here, 'README.txt')).read()
# CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'pyramid_jinja2',
    'waitress',
    ]

setup(name='unpub',
      version='0.0',
      description='unpub',
      # long_description=README + '\n\n' +  CHANGES,
      author='',
      author_email='',
      url='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="unpub",
      entry_points = """\
      [paste.app_factory]
      main = unpub:main
      """,
      )
