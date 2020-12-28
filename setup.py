#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='snyk-test',
    use_scm_version={
        'local_scheme': 'dirty-tag',
        'write_to': 'src/snyk_test/_version.py',
        'fallback_version': '0.0.2',
    },
    license='MIT',
    description='A package that wraps pysnyk library for easier usage from cli interfaces',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='Avishay Bar',
    author_email='avishay.il@gmail.com',
    url='https://github.com/avishayil/python-snyk-test',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities',
    ],
    project_urls={
        'Documentation': 'https://python-snyk-test.readthedocs.io/',
        'Changelog': 'https://python-snyk-test.readthedocs.io/en/latest/changelog.html',
        'Issue Tracker': 'https://github.com/avishayil/python-snyk-test/issues',
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires='>=3.7',
    install_requires=[
        'pysnyk',
        'pandas',
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    setup_requires=[
        'pytest-runner',
        'setuptools_scm>=3.3.1',
    ],
    entry_points={
        'console_scripts': [
            'snyk-test = snyk_test.cli:main',
        ]
    },
)
