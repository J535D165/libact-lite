#!/usr/bin/env python

from setuptools import setup


setup(
    name='libact-lite',
    version='0.1.3dev',
    description='Pool-based active learning in Python',
    long_description=open('README.md').read(),
    author='Jonathan de Bruin',
    author_email='jonathandebruinos@gmail.com',
    url='https://github.com/J535D165/libact-lite',
    classifiers=[
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    test_suite='libact',
    packages=[
        'libact',
        'libact.base',
        'libact.models',
        'libact.models.multilabel',
        'libact.labelers',
        'libact.query_strategies',
        'libact.query_strategies.multilabel',
        'libact.query_strategies.multiclass',
        'libact.utils',
    ],
    package_dir={
        'libact': 'libact',
        'libact.base': 'libact/base',
        'libact.models': 'libact/models',
        'libact.labelers': 'libact/labelers',
        'libact.query_strategies': 'libact/query_strategies',
        'libact.query_strategies.multiclass': 'libact/query_strategies/multiclass',
        'libact.utils': 'libact/utils',
    },
)
