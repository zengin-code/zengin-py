# -*- coding: utf-8 -*-

import sys
import os
import re

from setuptools import setup, find_packages


here = os.path.dirname(__file__)
package_path = os.path.join(here, 'zengin_code')

version = ''
with open(os.path.join(package_path, '__init__.py'), 'r') as f:
    version = re.compile(
        r".*__version__ = '(.*?)'\n", re.S).match(f.read()).group(1)

version = '{0}.{1}'.format(version, open(os.path.join(
    package_path, 'source-data', 'data', 'updated_at'
), 'r').read().strip())

readme = open(os.path.join(here, 'README.rst')).read()

requires = [
    'six',
]

setup_requires = [
   'pytest-runner',
]

tests_require = [
   'pytest-cov',
   'pytest',
]

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Software Development :: Libraries',
]


setup(
    name='zengin_code',
    version=version,
    description='bank codes and branch codes for Japanese.',
    long_description=readme,
    url='https://github.com/zengin-code/zengin-py',
    author='Zengin Code',
    author_email='zengin-code@zeny.io',
    classifiers=classifiers,
    keywords=['zengin', 'bank', 'japanese'],
    install_requires=requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    package_data={
        'zengin_code': [
            'source-data/data/md5', 'source-data/data/updated_at',
            'source-data/data/*.json', 'source-data/data/branches/*.json'
        ]
    },
    license='MIT',
)
