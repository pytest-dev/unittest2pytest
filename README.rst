==================================
unittest2pytest
==================================

-----------------------------------------------------
Helps converting unittest test-cases to pytest
-----------------------------------------------------

:Author:    Hartmut Goebel <h.goebel@crazy-compilers.com>
:Version:   Version 0.1
:Copyright: Hartmut Goebel
:Licence:   GNU Public Licence v3 or later (GPLv3+)
:Homepage:  https://github.com/htgoebel/unittest2pytest


.. image:: https://secure.travis-ci.org/htgoebel/unittest2pytest.png?branch=master
   :target: https://travis-ci.org/htgoebel/unittest2pytest/


`unittest2pytest` is a tool that helps rewriting Python `unittest`
test-cases into pytest_ test-cases.

In contrast to other similar tools, this `unittest2pytest`
- handles keyword arguments,
- handles single-line test-cases and several tests on one line,
- uses context-handlers where appropriate.

This is done by using ``lib2to3`` and Python's mighty ``inspect``
module.



Installation
===================

To install unittest2pytest, simply run::

    pip install unittest2pytest


Usage
===================

To print a diff of changes that unittest2pytest will make against a
particular source file or directory::

    unittest2pytest source_folder

To have those changes written to the files::

    unittest2pytest -w source_folder

To have those changes written to another directory::

    unittest2pytest -w source_folder --output-dir /some/where/else

By default, this will create backup files for each file that will be
changed. You can add the `-n` option to not create the backups. Please
do not do this if you are not using a version control system.

For more options about running particular fixers, run
``unittest2pytest --help`` or read the `lib2to3 documentation`_. This
tool is built on top of that one.


Fixes
===================

A list of the available fixers can be found with the following::

    $ unittest2pytest -l
    Available transformations for the -f/--fix option:
    remove_class
    self_assert


.. _`lib2to3 documentation`: http://docs.python.org/library/2to3.html
.. _pytest: http://www.python.org/dev/peps/pep-0008/


..
 Local Variables:
 mode: rst
 ispell-local-dictionary: "american"
 coding: utf-8
 End:
