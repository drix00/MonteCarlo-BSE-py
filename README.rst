=================
MonteCarlo-BSE-py
=================

Overview
========

Monte Carlo simulation of backscattered electron (BSE) in a SEM.

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |coveralls|
    * - package
      - |
        |


.. |docs| image:: https://readthedocs.org/projects/MonteCarlo-BSE-py/badge/?version=latest
    :target: https://MonteCarlo-BSE-py.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/drix00/MonteCarlo-BSE-py.svg?branch=master
    :target: https://travis-ci.org/drix00/MonteCarlo-BSE-py
    :alt: Travis-CI Build Status

.. |coveralls| image:: https://coveralls.io/repos/github/drix00/MonteCarlo-BSE-py/badge.svg?branch=master
    :target: https://coveralls.io/github/drix00/MonteCarlo-BSE-py?branch=master
    :alt: Coveralls Coverage Status


.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/pytest-dev/pytest-cov?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/pytestbot/pytest-cov

.. |requires| image:: https://requires.io/github/pytest-dev/pytest-cov/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/pytest-dev/pytest-cov/requirements/?branch=master

.. |version| image:: https://img.shields.io/pypi/v/pytest-cov.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pytest-cov

.. |conda-forge| image:: https://img.shields.io/conda/vn/conda-forge/pytest-cov.svg
    :target: https://anaconda.org/conda-forge/pytest-cov

.. |commits-since| image:: https://img.shields.io/github/commits-since/pytest-dev/pytest-cov/v2.7.1.svg
    :target: https://github.com/pytest-dev/pytest-cov/compare/v2.7.1...master
    :alt: Commits since latest release

.. |wheel| image:: https://img.shields.io/pypi/wheel/pytest-cov.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/pytest-cov

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pytest-cov.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/pytest-cov

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pytest-cov.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/pytest-cov

.. end-badges


Development
===========

In the *MonteCarlo-BSE-py folder*, run to install the project in develop mode

.. code:: shell

   pip install -e .[develop]

Build the documentation:

.. code-block:: console

    $ cd docs
    $ make html

Add or modify the API documentation:

.. code-block:: console

    $ cd docs
    $ sphinx-apidoc -o api -e -f -P ../mcbse
    $ make html

Before committing your modification.

In the *MonteCarlo-BSE-py folder*, run the tests:

.. code-block:: console

    $ pytest -v

check the code style:

.. code-block:: console

    $ pycodestyle .
    $ pyflakes .


To do
-----

.. todolist::
