#!/usr/bin/env python

from pydgutils_bootstrap import use_pydgutils
use_pydgutils()

import pydgutils
import sys
from setuptools import setup, find_packages

with open('README.rst') as readme_file, open('HISTORY.rst') as history_file:
    long_description = (readme_file.read() + "\n\n" + history_file.read())

install_requires = [
    'click>=6.0',
    "jsonpickle",
    "simplejson",
    "PyYaml",
]

setup_requires = [
    'pytest-runner',
    # TODO(starofrainnight): put setup requirements (distutils extensions, etc.) here
]

tests_requires = [
    'pytest',
    'click>=6.0',
    # TODO: put package test requirements here
]

source_dir = pydgutils.process()

packages = find_packages(where=source_dir)

setup(
    name='serializabledict',
    version='0.0.4',
    description="A simple serializable dict",
    long_description=long_description,
    author="Hong-She Liang",
    author_email='starofrainnight@gmail.com',
    url='https://github.com/starofrainnight/serializabledict',
    package_dir={"": source_dir},
    packages=packages,
    include_package_data=True,
    install_requires=install_requires,
    license="Apache Software License",
    zip_safe=False,
    keywords='serializabledict,serializabledict',
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=tests_requires,
    setup_requires=setup_requires,
)
