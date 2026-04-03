Changelog
============

UNRELEASED
----------

*UNRELEASED*

- Switch from lib2to3 to `fissix <https://github.com/amyreese/fissix>`_,
  a maintained fork of lib2to3 (`#95`_).

- Add Python 3.13, 3.14, and 3.15 support.

- Migrate packaging from ``setup.py`` to ``pyproject.toml`` with
  PEP 639 SPDX license metadata (``GPL-3.0-or-later``) (`#96`_).

- Use ``setuptools-scm`` for version management. Versions are now
  derived from git tags (`#97`_).

- Add ``check_changelog.py`` CI check to enforce changelog entries
  (`#97`_).

- Gate PyPI publishing on tests passing by merging the release
  workflow into CI (`#97`_).

- Update installation instructions with ``uv tool install`` (`#92`_).

.. _#92: https://github.com/pytest-dev/unittest2pytest/pull/92
.. _#95: https://github.com/pytest-dev/unittest2pytest/pull/95
.. _#96: https://github.com/pytest-dev/unittest2pytest/pull/96
.. _#97: https://github.com/pytest-dev/unittest2pytest/pull/97


0.5
---

*2024-12-10*


- Convert ``self.fail()`` to ``pytest.fail()`` (`#39`_).

- Python >=3.9 is now required.

- Allow non-string keys when translating ``assertDictContainsSubset`` (`#54`_).

.. _#39: https://github.com/pytest-dev/unittest2pytest/issues/39
.. _#54: https://github.com/pytest-dev/unittest2pytest/issues/54



0.4 (2019-06-30)
----------------

* Add support for ``assertDictContainsSubset``.

* Put parenthesis around expressions if required.

* Fixed assertRaisesRegex, assertRaisesRegexp and assertWarnsRegex.
  The regex was getting replaced with an undefined variable `pattern`.

* Fix assertRaisesRegex and assertRaisesRegexp with `**kwargs` and
  `atom` parameters.

* Made assertRaisesRegex, assertRaisesRegexp and assertWarnsRegex use
  the `match` kwarg in `pytest.raises` instead of creating a variable
  with the context manager and doing an assert on `re.search`.


* Add a short developer guide.

* Remove testing on Python 3.0, 3.1, 3.2, add 3.6 and 3.7.

* Distribute package as a universal wheel.


v0.3 (2016-07-26)
------------------

* Add support for assertRaises / assertWarns context managers.

* Add support for converting lambda arguments in assertRaises into
  context managers.

* Fix some incorrect transformations.

* Internal cleanup and fixes.


v0.2 (2015-10-20)
---------------------

* Add support for assertRegex/assertRegexpMatches, assertNotRegex,
  assertRaisesRegex/assertRaisesRegexp, assertWarnsRegex.

* `unittest2pytest` is now a `pytest` subproject.

* Minor fixes.


v0.1 (2015-10-16)
---------------------

* Initial release

..
 Local Variables:
 mode: rst
 ispell-local-dictionary: "american"
 coding: utf-8
 End:
