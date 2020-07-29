========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor|
        | |coveralls| |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-snyk-test/badge/?style=flat
    :target: https://readthedocs.org/projects/python-snyk-test
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.com/avishayil/python-snyk-test.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/avishayil/python-snyk-test

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/avishayil/python-snyk-test?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/avishayil/python-snyk-test

.. |coveralls| image:: https://coveralls.io/repos/avishayil/python-snyk-test/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/avishayil/python-snyk-test

.. |codecov| image:: https://codecov.io/gh/avishayil/python-snyk-test/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/avishayil/python-snyk-test

.. |version| image:: https://img.shields.io/pypi/v/snyk-test.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/snyk-test

.. |wheel| image:: https://img.shields.io/pypi/wheel/snyk-test.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/snyk-test

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/snyk-test.svg
    :alt: Supported versions
    :target: https://pypi.org/project/snyk-test

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/snyk-test.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/snyk-test

.. |commits-since| image:: https://img.shields.io/github/commits-since/avishayil/python-snyk-test/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/avishayil/python-snyk-test/compare/v0.0.1...master



.. end-badges

A package that wraps pysnyk library for easier usage from cli interfaces

* Free software: MIT license

Installation
============

::

    $ brew reinstall readline xz # OSX only
    If you're using pyenv, reinstall it # OSX only

Then install the package using ``pip``

::

    pip install snyk-test --no-deps && pip install snyk-test

You can also install the in-development version with::

    pip install https://github.com/avishayil/python-snyk-test/archive/master.zip


Documentation
=============

First, before using ``snyk-test`` you must authenticate with ``snyk`` using ``snyk auth``
Then, alter your ``$HOME/.config/configstore/snyk.json`` and add the ``org_id`` parameter to the JSON file using the following command::

    $ snyk config set org_id=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx # Your organization ID

The JSON file will look as follows::

    {
	    "api": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
	    "org_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }

Then, after all the prerequisites are met, run the the following command from your terminal::

    snyk-test package@version

For Example::

    $ snyk-test channels-redis@2.4.2


Documentation
=============


https://python-snyk-test.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
