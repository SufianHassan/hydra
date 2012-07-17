#!/usr/bin/env python
from setuptools import setup
setup(
    name = 'hydra',
    version = '0.11',
    author = "Michael D'Agosta",
    author_email = 'mdagosta@codebug.com',
    description = 'Hydra Tornado utilities',
    url = 'https://github.com/mdagosta/hydra',
    packages = ['hydra'],
    install_requires = [
        'distribute',
        'tornado == 2.3',
    ],
    )
