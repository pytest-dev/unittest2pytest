Changelog
============

v0.4 (unreleased)
-----------------

- Fixed assertRaisesRegex, assertRaisesRegexp and assertWarnsRegex.  The regex
  was getting replaced with an undefined variable `pattern`.
- Made assertRaisesRegex, assertRaisesRegexp and assertWarnsRegex use the
  `match` kwarg in `pytest.raises` instead of creating a variable with the
  context manager and doing an assert on `re.search`.


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
