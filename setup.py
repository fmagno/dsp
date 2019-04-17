#!/usr/bin/env python


from setuptools import setup, find_packages

version = '0.0.1'


# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    name='dsp',
    version=version,
    author='fmagno',
    author_email='flmagnom@gmail.com',
    packages=find_packages(),
    install_requires=[
        'future-fstrings',
        'matplotlib',
        'numpy',
        'toml',
        'namedlist',
    ],
    scripts=[
        'scripts/geom2freq',
        'scripts/sig_viewer',
        'scripts/sine_gen',
        'scripts/run_xp',
    ]
)
