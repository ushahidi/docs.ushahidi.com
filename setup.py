import os
import sys

from setuptools import setup, find_packages

install_requires=[
    'setuptools'
    ]

tests_require = [
    'WebTest >= 1.3.1', # py3 compat
    ]

docs_extras = [
    'Sphinx >= 1.3.1',
    'docutils',
    'ushahidi-sphinx-rtd-theme'
    ]


setup(name='Ushahidi Platform Docs',
      version='0.1',
      description='Ushahidi Platform Docs',
      keywords='ushahidi docs',
      author="Will Doran",
      author_email="will@ushahidi.com",
      url="http://ushahidi.com",
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires = install_requires,
      extras_require = {
          'docs':docs_extras,
          }
      )
