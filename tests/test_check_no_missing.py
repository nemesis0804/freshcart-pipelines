"""
tests/test_check_no_missing.py
--------------------------------
Part C4 — pytest coverage for the check_no_missing custom transformer block.

Independent improvement (Neelanjana Prakash, 23BCS176):
The original test suite had no independent pytest coverage for the custom
check_no_missing block (C4). Its correctness was only verified inside Mage's
DAG runner, meaning CI would not catch regressions. These tests import the
block directly (using the same import shim as prepare_data) and run under
pytest in GitHub Actions.

Note: We import the module object (not the test_* function by name) to avoid
pytest collecting the Mage @test function as a pytest test case.
"""

import pandas as pd
import pytest
import iris_project.transformers.check_no_missing as _cnm_mod


class TestCheckNoMissing:
    """Tests for the check_no_missing transformer block."""

    def test_passes_on_clean_iris(self, iris_df):
        """Block must return the dataframe unchanged when data is clean."""
        result = _cnm_mod.check_data(iris_df)
        assert result is not None
        assert len(result) == 150

    def test_output_identical_to_input(self, iris_df):
        """Block is a pass-through; output must equal input."""
        result = _cnm_mod.check_data(iris_df)
        pd.testing.assert_frame_equal(result, iris_df)

    def test_quality_gate_passes_on_clean_iris(self, iris_df):
        """Mage @test test_data_quality must not raise for the clean Iris dataset."""
        result = _cnm_mod.check_data(iris_df)
        # Call via module to avoid pytest collecting this name as a test
        _cnm_mod.test_data_quality(result)

    def test_quality_gate_detects_nulls(self, iris_df):
        """Mage @test must raise AssertionError when nulls are introduced."""
        dirty = iris_df.copy()
        dirty.loc[0, 'sepal length (cm)'] = None
        result = _cnm_mod.check_data(dirty)
        with pytest.raises(AssertionError, match="missing values"):
            _cnm_mod.test_data_quality(result)

    def test_quality_gate_detects_wrong_class_count(self, iris_df):
        """Mage @test must raise AssertionError when target has fewer than 3 classes."""
        two_class = iris_df[iris_df['target'] != 2].copy()
        result = _cnm_mod.check_data(two_class)
        with pytest.raises(AssertionError, match="3 classes"):
            _cnm_mod.test_data_quality(result)
