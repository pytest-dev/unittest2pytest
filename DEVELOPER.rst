
Testing
===========

Continuous integration tests are available at
https://github.com/pytest-dev/unittest2pytest/actions.

Prior to pushing a pull request to GitHub, please test locally::

  pip install tox pytest
  tox  -e py


Version Scheme
=================

Regarding the version scheme, unittest2pytest conforms to :PEP:`440`.
This basically means that releases will look like `0.3`, `0.3.1`,
`0.4`, and pre-releases will have versions like `0.3.dev1`,
`0.3.1.dev0`.




.. _PyPI: https://pypi.python.org/
.. _TestPyPI: https://testpypi.python.org/pypi
.. |unittest2pytest@PyPI| replace:: unittest2pytest at PyPI
.. _unittest2pytest@PyPI: https://pypi.python.org/unittest2pytest

..
 Local Variables:
 mode: rst
 ispell-local-dictionary: "american"
 coding: utf-8
 End:
