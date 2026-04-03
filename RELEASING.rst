=========================
Releasing unittest2pytest
=========================

``unittest2pytest`` uses `setuptools-scm`_ for version management.
Versions are derived automatically from git tags.

.. _setuptools-scm: https://github.com/pypa/setuptools-scm


Relative bump
-------------

Run the **Release** workflow, selecting the version bump type:

.. code-block:: console

     gh workflow run release.yml -R pytest-dev/unittest2pytest --field bump=minor

Options: ``major``, ``minor``, ``micro``, ``post``.  The version is
computed automatically from the latest git tag.


Absolute version
----------------

To release a specific version (e.g. a release candidate):

.. code-block:: console

     gh workflow run release.yml -R pytest-dev/unittest2pytest --field version=1.0rc1


What the workflow does
----------------------

#. Runs ``scripts/make_changelog.py`` to replace the ``UNRELEASED`` section
   with the version number and today's date.
#. Commits, tags, and pushes.
#. Builds the package.
#. Creates a GitHub Release with the built artifacts.
#. Publishes to PyPI (requires the ``release`` environment).
#. Runs ``scripts/make_changelog.py UNRELEASED`` and pushes a follow-up commit.


How versioning works
--------------------

- Tagged commits (e.g. ``v0.6``) produce version ``0.6``.
- Commits after a tag produce dev versions like ``0.7.dev3+gabcdef``.
- The version is written to ``unittest2pytest/_version.py`` at build
  time.  This file is git-ignored and should not be committed.
