=========================
Releasing unittest2pytest
=========================

``unittest2pytest`` uses `setuptools-scm`_ for version management.
Versions are derived automatically from git tags.

.. _setuptools-scm: https://github.com/pypa/setuptools-scm


Version
-------

``main`` should always be green and a potential release candidate.
``unittest2pytest`` follows semantic versioning, so given that the
current version is ``X.Y.Z``, to find the next version number one
needs to look at the ``CHANGELOG.rst`` file:

- If there any new feature, then we must make a new **minor** release:
  next release will be ``X.Y+1.0``.

- Otherwise it is just a **bug fix** release: ``X.Y.Z+1``.


Steps
-----

To publish a new release ``X.Y.Z``, the steps are as follows:

#. Update ``CHANGELOG.rst``:

   .. code-block:: console

        python make_changelog.py X.Y.Z

   This replaces the ``UNRELEASED`` section with a dated ``X.Y.Z``
   section.  Review the result and add any missing entries before
   committing.

#. Commit and push:

   .. code-block:: console

        git commit -am "Prepare release X.Y.Z"
        git push origin main

#. Tag and push:

   .. code-block:: console

        git tag -s vX.Y.Z -m "unittest2pytest X.Y.Z"
        git push origin vX.Y.Z

   Pushing the tag triggers the CI workflow, which builds, tests,
   publishes to PyPI, and creates a GitHub release.

#. Start the next development cycle:

   .. code-block:: console

        python make_changelog.py UNRELEASED
        git commit -am "Start next development cycle"
        git push origin main


How versioning works
--------------------

- Tagged commits (e.g. ``v0.6``) produce version ``0.6``.
- Commits after a tag produce dev versions like ``0.7.dev3+gabcdef``.
- The version is written to ``unittest2pytest/_version.py`` at build
  time.  This file is git-ignored and should not be committed.
