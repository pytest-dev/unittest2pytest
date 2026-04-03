# Release Process

unittest2pytest uses [setuptools-scm](https://github.com/pypa/setuptools-scm)
for version management. Versions are derived automatically from git tags.

## Cutting a Release

1. **Update `CHANGELOG.rst`:**

   ```
   python make_changelog.py X.Y.Z
   git commit -am "Prepare release X.Y.Z"
   git push origin main
   ```

   This replaces the `UNRELEASED` section with a dated `X.Y.Z` section.
   Review the result and add any missing entries before committing.

2. **Tag and push:**

   ```
   git tag -s vX.Y.Z -m "unittest2pytest X.Y.Z"
   git push origin vX.Y.Z
   ```

   Pushing the tag triggers the release workflow, which builds,
   publishes to PyPI, and creates a GitHub release.

3. **Start the next development cycle:**

   ```
   python make_changelog.py UNRELEASED
   git commit -am "Start next development cycle"
   git push origin main
   ```

## How Versioning Works

- Tagged commits (e.g. `v0.6`) produce version `0.6`.
- Commits after a tag produce dev versions like `0.7.dev3+gabcdef`.
- The version is written to `unittest2pytest/_version.py` at build time.
  This file is git-ignored and should not be committed.
