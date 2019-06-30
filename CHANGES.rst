Changelog
============

0.5 (unreleased)
----------------

- Nothing changed yet.


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
