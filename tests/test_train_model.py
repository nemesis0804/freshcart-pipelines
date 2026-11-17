"""
tests/test_train_model.py
--------------------------
pytest coverage for the train_model transformer block.

Independent improvement (Neelanjana Prakash, 23BCS176):
The original suite had no standalone pytest for train_model. Its @test quality
gate was only exercised inside the Mage DAG runner (run_pipeline.py), which
isn't invoked by CI. These tests run the block directly and verify:
  - The model trains and produces predictions.
  - Accuracy is correctly computed.
  - The @test gate passes for depth >= 2 and fails for depth = 1.
  - The iris_model.pkl artefact is created (but ignored by .gitignore).

Note: We import via the module object to avoid pytest collecting the Mage
@test function (test_accuracy) as a pytest test case.
"""

import os
import pytest
import iris_project.transformers.train_model as _tm_mod


class TestTrainModel:
    """Tests for the train_model transformer block."""

    def test_predictions_column_exists(self, prepared_df):
        """Output DataFrame must contain a 'predicted' column."""
        result = _tm_mod.train(prepared_df, max_depth=3)
        assert 'predicted' in result.columns

    def test_output_is_test_split_only(self, prepared_df):
        """train() returns only the test rows (30 rows for 80/20 split)."""
        result = _tm_mod.train(prepared_df, max_depth=3)
        assert len(result) == 30

    def test_accuracy_above_threshold_depth3(self, prepared_df):
        """At max_depth=3, accuracy must be >= 0.80 (the assignment threshold)."""
        result = _tm_mod.train(prepared_df, max_depth=3)
        accuracy = (result['predicted'] == result['target']).mean()
        assert accuracy >= 0.80

    def test_quality_gate_passes_depth3(self, prepared_df):
        """Mage @test test_accuracy must not raise for max_depth=3."""
        result = _tm_mod.train(prepared_df, max_depth=3)
        _tm_mod.test_accuracy(result)

    def test_quality_gate_fails_depth1(self, prepared_df):
        """Mage @test test_accuracy must raise AssertionError for max_depth=1 (underfitting)."""
        result = _tm_mod.train(prepared_df, max_depth=1)
        with pytest.raises(AssertionError, match="80%"):
            _tm_mod.test_accuracy(result)

    def test_pkl_file_written(self, prepared_df, tmp_path, monkeypatch):
        """train() must write iris_model.pkl (the file is .gitignored, not committed)."""
        monkeypatch.chdir(tmp_path)
        _tm_mod.train(prepared_df, max_depth=3)
        assert os.path.exists("iris_model.pkl")
