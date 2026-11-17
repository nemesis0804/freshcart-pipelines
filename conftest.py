"""
conftest.py (root level)
------------------------
Root-level pytest configuration.

The Mage @test decorated functions in iris_project/transformers/ are named
test_* and take a positional 'output' argument.  When pytest imports those
modules (because our test files import from them), it tries to collect those
functions as test cases and fails with "fixture 'output' not found".

Using collect_ignore_glob here (at the rootdir conftest) prevents pytest
from directly scanning or collecting those source files as test modules.
The functions are still callable as normal Python functions from our tests.
"""

collect_ignore_glob = [
    "iris_project/**/*.py",
    "elt/**/*.py",
    "stream/**/*.py",
]
