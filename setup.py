#!/usr/bin/env python
import os

from setuptools import setup

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md')) as f:
    long_description = f.read()

setup(
    name='keras-resnet',
    version='0.0.1',
    description='Residual networks implementation using Keras-1.0 functional API',
    long_description=long_description,
    url='https://github.com/raghakot/keras-resnet',
    author='raghakot',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='keras resnet residual-networks deep-learning cnn',
    py_modules=['resnet'],
    install_requires=['keras>=1.0', 'six'],
    extras_require={
        'test': ['pytest'],
    },
)
