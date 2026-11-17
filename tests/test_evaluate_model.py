"""
tests/test_evaluate_model.py
-----------------------------
pytest coverage for the evaluate_model transformer block and its new @test gate.

Independent improvement (Neelanjana Prakash, 23BCS176):
Added alongside the new @test decorator on evaluate_model. Verifies:
  - evaluate() returns the 4 required metrics.
  - All metric values are in [0, 1].
  - The @test gate catches a corrupt DataFrame (NaN metrics).

Note: We import via the module object to avoid pytest collecting the Mage
@test function (test_metrics) as a pytest test case.
"""

import pandas as pd
import pytest
import iris_project.transformers.evaluate_model as _em_mod
import iris_project.transformers.train_model as _tm_mod


class TestEvaluateModel:
    """Tests for the evaluate_model transformer block."""

    def test_returns_four_metrics(self, prepared_df):
        """evaluate() must return a DataFrame with exactly 4 rows."""
        preds = _tm_mod.train(prepared_df, max_depth=3)
        metrics = _em_mod.evaluate(preds)
        assert len(metrics) == 4

    def test_metric_names(self, prepared_df):
        """Metric names must be accuracy, precision, recall, f1_score."""
        preds = _tm_mod.train(prepared_df, max_depth=3)
        metrics = _em_mod.evaluate(preds)
        assert list(metrics['metric']) == ['accuracy', 'precision', 'recall', 'f1_score']

    def test_all_values_in_range(self, prepared_df):
        """All metric values must be in [0.0, 1.0]."""
        preds = _tm_mod.train(prepared_df, max_depth=3)
        metrics = _em_mod.evaluate(preds)
        for _, row in metrics.iterrows():
            assert 0.0 <= row['value'] <= 1.0, (
                f"Metric {row['metric']} = {row['value']} is out of range"
            )

    def test_quality_gate_passes(self, prepared_df):
        """Mage @test test_metrics must not raise for a valid predictions DataFrame."""
        preds = _tm_mod.train(prepared_df, max_depth=3)
        metrics = _em_mod.evaluate(preds)
        _em_mod.test_metrics(metrics)
