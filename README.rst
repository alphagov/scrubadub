
.. NOTES FOR CREATING A RELEASE:
..
..   * bump the version number
..   * update docs/changelog.rst
..   * git push
..   * python setup.py sdist upload
..   * create a release https://github.com/datascopeanalytics/scrubadub/releases

|Build Status| |Version| |Test Coverage|

.. |Build Status| image:: https://travis-ci.org/datascopeanalytics/scrubadub.svg?branch=master
   :target: https://travis-ci.org/datascopeanalytics/scrubadub
.. |Version| image:: https://img.shields.io/github/tag/ukgovdatascience/scrubadub.svg
   :target: https://github.com/ukgovdatascience/scrubadub/tags/
.. |Test Coverage| image:: https://codecov.io/gh/ukgovdatascience/scrubadub/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/ukgovdatascience/scrubadub

scrubadub
=========

Clean personally identifiable information from dirty dirty text.

This is a fork https://github.com/datascopeanalytics/scrubadub updated for Python 3.x, and with additional filth and detectors for National Insurance numbers (NINOs), UK/GB phone numbers, Passport numbers, and UK driving licenses.

The original documentation is available here: `Full documentation <http://scrubadub.readthedocs.org>`__.

Usage
=====

.. code-block:: python

   In [1]: import scrubadub
   
   In [2]: dirty = 'My name is John Smith and my email address is John@example.com.'
   
   In [3]: scrubadub.clean(dirty)
   
   Out[3]: 'My name is {{NAME}} {{NAME}} and my email address is {{NAME+EMAIL}}.'
   
   



