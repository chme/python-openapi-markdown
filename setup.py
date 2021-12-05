#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='openapi-markdown',
    version='0.1.0',
    license='MIT',
    description='OpenAPI markdown generator',
    long_description='',
    author='Christian Meffert',
    author_email='christian.meffert@googlemail.com',
    url='https://github.com/chme',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # classifiers: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
    keywords=[
    ],
    install_requires=[
        'prance',
        'Jinja2',
        'markdown',
        'click',
    ],
    extras_require={
    },
    entry_points={
        'console_scripts': [
            'openapi-markdown = openapi_markdown.cli:main',
        ]
    },
)
