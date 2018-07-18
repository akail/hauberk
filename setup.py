#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read()

setup_requirements = ['pytest-runner', ]

with open('requirements_test.txt') as requirements_test_file:
    test_requirements = requirements_test_file.read()

setup(
    author="Andrew Kail",
    author_email='andrew.a.kail@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Hauberk allows you to created advanced email automations using python",
    entry_points={
        'console_scripts': [
            'hauberk=hauberk.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='hauberk',
    name='hauberk',
    package_dir={"": "src"},
    packages=find_packages(include=['hauberk']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/akail/hauberk',
    version='0.1.0',
    zip_safe=False,
)
