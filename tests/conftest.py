"""
tests/conftest.py
-----------------
Shared pytest fixtures for the FreshCart Pipelines test suite.

Independent improvement (Neelanjana Prakash, 23BCS176):
The original test files each called load_iris(as_frame=True).frame inline,
repeating the same 3-line setup in every test. This conftest.py extracts
that setup into a single shared fixture (DRY principle), making tests
shorter and easier to maintain.

Also handles the pytest collection issue: Mage @test decorated functions
in iris_project/transformers/ are named test_* and have a positional
'output' parameter. When our test files import those modules, pytest
tries to collect those functions as test cases and fails with
"fixture 'output' not found". The collect_ignore_glob below prevents that.
"""

import pytest
from sklearn.datasets import load_iris


# ---------------------------------------------------------------------------
# Prevent pytest from collecting Mage @test functions from transformer files.
# Those functions are named test_* but expect a positional 'output' argument
# (not a pytest fixture), so pytest errors with "fixture 'output' not found".
# ---------------------------------------------------------------------------
collect_ignore_glob = [
    "../iris_project/transformers/*.py",
    "../iris_project/data_loaders/*.py",
    "../iris_project/data_exporters/*.py",
]


@pytest.fixture(scope="session")
def iris_df():
    """Return the full 150-row sklearn Iris DataFrame (session-scoped, loaded once)."""
    return load_iris(as_frame=True).frame


@pytest.fixture(scope="session")
def prepared_df(iris_df):
    """Return the iris_df after the prepare_data transform (120 train / 30 test rows)."""
    from iris_project.transformers.prepare_data import transform
    return transform(iris_df)
