
Testing
===========

Continuous integration tests are available at
https://github.com/pytest-dev/unittest2pytest/actions.

Prior to pushing a pull request to GitHub, please test locally::

  pip install tox pytest
  tox  # or tox -e py37,py38,py39


Version Scheme
=================

Regarding the version scheme, unittest2pytest conforms to :PEP:`440`.
This basically means that releases will look like `0.3`, `0.3.1`,
`0.4`, and pre-releases will have versions like `0.3.dev1`,
`0.3.1.dev0`.


How to Release
=================


Preparation
-----------------

1. Get yourself an account at PyPI_ and TestPyPI_. Fill both
   credentials in your `~/.pypirc` file, as `described in the Python
   Wiki <https://wiki.python.org/moin/TestPyPI>`_.

   * In difference to that description, list `pypitest` *first*. This
     will make `zest.releaser` push the release there first giving you
     a chance for last minute fixes.

2. Install `docutils` and `zest.releaser`, a helper for automating
   releasing a Python project::

     pip install --user docutils zest.releaser


Full Release Process
---------------------

1. Prepare (see above).

2. Implement and close all issues and pull requests in a specific
   milestone.

3. Ensure everything relevant is committed and tested. ``git stash``
   your local changes which should not go into the release.

4. Be sure that the current code passes tests locally::

     tox -e py37,py38,py39

5. Be sure `CI tests
   <https://github.com/pytest-dev/unittest2pytest/actions>`_ pass.


Now we start with the main release process.

6. Set shell variables to be able to copy-and-paste the remaining
   snippets, e.g.::

      version=0.3
      prev_version=0.2

7. Create the **release branch**::

      git checkout -b release/$version

8. **Update versions** in source-code, Changelog, etc.::

      prerelease # zest.releaser command

   This will

   - ask you a few questions - required version, etc.
   - remove `.devN` from the version string
   - update date and version in `CHANGES.rst`

9. Update **``CHANGES.rst``** and **``AUTHORS``**.

    Where to look for possible changes? You can look in pull requests,
    issues, commits, mailing list or even the tool's cli options
    (new/removed options).

    Authors should be updated based on merged pull requests::

       git shortlog --numbered --summary --email v${prev_version}..HEAD

    a. Check if the files are valid reStructuredText by running::

        rst2html CHANGES.rst > /tmp/CHANGES.html
        xdg-open /tmp/CHANGES.html  # opens file in your web-browser

    b. If everything is fine, commit::

        git commit -m "Update CHANGES and AUTHORS for release $version" \
           CHANGES.rst AUTHORS.txt


10. In the **README**, update the versions in the badge-images and
    related links.

    a. Verify the result be running::

         git diff --color-words='.' README.rst

    b. Again, check if the files are valid reStructuredText by running::

        rst2html README.rst > /tmp/README.html
        xdg-open /tmp/README.html  # opens file in your web-browser

    c. If everything is fine, commit::

        git commit -m 'Update versions in README.' README.rst
        README_CHANGE=$(git rev-parse --short HEAD) # remember this commit

11. Adjust whatever else is required for the release *now*.


12. Complete the release:

    a. Merge into branch `master`::

          git checkout master
          git merge --no-ff -X theirs -m "Finished release $version." \
             release/$version

    b. In case of a merge-conflict, resolve it using::

	 git gui # In the context-menu select "Use Local Version"
	 git commit -m "Release $version."


13. Run the release script ``release`` and it will do:

    - create a signed tag for the released version
    - create and sign source archives
    - uploads them to PyPI

    ::

      release # zest.releaser command

    Submit to `testpypi` first! You can not change any file after
    you've uploaded it to PyPI!

14. Push the  changes::

       git push --follow-tags origin master

15. Create release on GitHub:

    a. Go to the `unittest2pytest release page
       <https://github.com/pytest-dev/unittest2pytest/releases>`_

    b. Edit the latest `tag` details.

    c. Copy there changelog for the current release. This should look
       like `this one
       <https://github.com/pytest-dev/unittest2pytest/releases/tag/v0.3>`_

    d. Upload the `.tar.gz`- and `.zip`-archives and GPG-signatures
       that where uploaded to |unittest2pytest@PyPI|_

       Note: If you are using stuff like RequestBlocker or NoScript in
       your web-browser, mind to allow some additional access.


Now we are going to perform some **post-release** steps:

16. Forward the release-branch to master and check it out::

       git checkout master
       git branch -f release/$version master
       git checkout release/$version

17. Revert the version-related to the README (using the commit we
    remembered earlier)::

      git revert $README_CHANGE

18. Run the release script ``postrelease``::

      postrelease # zest.releaser command

    This will

    - increment version string for a new release: `3.0 -> 3.1.dev0`
    - prepare `CHANGES.rst` for the next release.

    You need to manually check the `README` and the version in
    `CHANGES`.

19. Merge into branch `develop`::

      git checkout develop
      git merge --no-ff -m "Finished release $version." release/$version

20. Check the diffs: it should only be version related stuff::

      git diff origin/develop

21. Push the  changes and delete the local release branch::

       git push --follow-tags origin develop master
       git branch -d release/$version


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
