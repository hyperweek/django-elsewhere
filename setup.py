#!/usr/bin/env python

from distutils.core import setup

setup(name='django-elsewhere',
      version='1.0',
      description='Formerly Django-PSN (Portable Social Networks) and originally created for Pownce.',
      author='Leah Culver',
      author_email='leah@sixapart.com',
      maintainer='Brian Neal',
      maintainer_email='bgneal@gmail.com',
      url='https://github.com/gremmie/django-elsewhere',
      packages=['elsewhere'],
      package_data={'elsewhere': ['static/elsewhere/*']},
      )
