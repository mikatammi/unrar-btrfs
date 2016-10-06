#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='unrar_btrfs',
    version='0.0.1',
    description="Experimental UnRAR tool which uses btrfs_clone to "
                 "\"decompress\" uncompressed split-RARs to save disk space",
    long_description=readme + '\n\n' + history,
    author="Mika Tammi",
    author_email='mikatammi@gmail.com',
    url='https://github.com/mikatammi/unrar_btrfs',
    packages=[
        'unrar_btrfs',
    ],
    package_dir={'unrar_btrfs':
                 'unrar_btrfs'},
    entry_points={
        'console_scripts': [
            'unrar-btrfs=unrar_btrfs.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='unrar_btrfs',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
