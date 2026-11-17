# CHANGELOG
## FreshCart Pipelines — From Git to Gold
**Student:** Neelanjana Prakash | **Roll Number:** 23BCS176  
**Reference Repository:** https://github.com/mxnsi04/freshcart-pipelines (Mansi Grover, 23BCS159)

All changes below are independent modifications made by Neelanjana Prakash on top of the reference implementation. The original Git history is preserved and unmodified.

---

## [Unreleased] — 2026-11-17

### Identity & Attribution
- Updated `README.md` author to Neelanjana Prakash / 23BCS176.
- Added §8 Source Attribution section in `README.md` clearly distinguishing inherited vs independently modified components.
- Updated headers in `ASSIGNMENT_TRACKER.md`, `SUBMISSION_CHECKLIST.md`, `VIVA_PREPARATION.md`, `evidence/evidence_index.md`.
- Corrected PDF filename to `23BCS176_Neelanjana_Prakash_Pipelines.pdf` across all documentation and generator scripts.
- Fixed incorrect attribution in SUBMISSION_CHECKLIST (original author correctly identified as Mansi Grover / 23BCS159).

### Bug Fix — B5 Quality Check (Critical)
- **File:** `elt/pipeline_runner.py` line 442
- **Bug:** `:` (dict key access, a no-op expression) was used instead of `=` (assignment).
- **Effect:** The sixth data-quality check (`orders_count_non_zero`) was silently never appended to the quality checks list and never executed.
- **Fix:** Changed `:` to `=` so the check is correctly registered.
- **Comment added** explaining the purpose of the sixth check.

### Environment Variable Validation
- **File:** `elt/pipeline_runner.py` `get_connection()` function
- Added explicit validation of required Snowflake environment variables at connection time.
- Raises `EnvironmentError` with a clear message if any of `SNOWFLAKE_ACCOUNT`, `SNOWFLAKE_USER`, `SNOWFLAKE_PASSWORD`, `SNOWFLAKE_DATABASE`, `SNOWFLAKE_SCHEMA`, `SNOWFLAKE_WAREHOUSE` are missing.
- Prevents silent failures when `.env` is not configured.

### New Independent Tests
- **`tests/conftest.py`** — Shared session-scoped pytest fixtures: `iris_df` and `prepared_df`.
- **`tests/test_check_no_missing.py`** — 5 tests for the `check_no_missing` transformer (C4 block):
  - `test_passes_on_clean_iris` — full Iris dataset passes without raising.
  - `test_output_identical_to_input` — block returns unmodified DataFrame.
  - `test_quality_gate_passes_on_clean_iris` — `@test` gate accepts clean data.
  - `test_quality_gate_detects_nulls` — gate fails when nulls injected.
  - `test_quality_gate_detects_wrong_class_count` — gate fails when target has wrong classes.
- **`tests/test_train_model.py`** — 6 tests for the `train_model` transformer:
  - `test_predictions_column_exists` — output DataFrame has `predictions` column.
  - `test_output_is_test_split_only` — output has 30 rows (20% of 150).
  - `test_accuracy_above_threshold_depth3` — depth=3 achieves ≥ 80% accuracy.
  - `test_quality_gate_passes_depth3` — `@test` gate passes at depth=3.
  - `test_quality_gate_fails_depth1` — `@test` gate correctly fails at depth=1.
  - `test_pkl_file_written` — `iris_model.pkl` is created after training.
- **`tests/test_evaluate_model.py`** — 4 tests for the `evaluate_model` transformer:
  - `test_returns_four_metrics` — dict has exactly 4 keys.
  - `test_metric_names` — dict contains accuracy, precision, recall, f1_score.
  - `test_all_values_in_range` — all metric values are in [0.0, 1.0].
  - `test_quality_gate_passes` — `@test test_metrics` gate passes.

### evaluate_model Enhancement
- **File:** `iris_project/transformers/evaluate_model.py`
- Added `@test` decorator function `test_metrics` asserting all 4 metric values are in [0, 1].
- This satisfies the assignment requirement for a testable evaluation branch.

### pytest Configuration
- **File:** `pytest.ini`
- Added `norecursedirs` to prevent pytest from scanning `iris_project/`, `elt/`, `stream/` directories.
- Added `testpaths = tests` to scope test discovery to the `tests/` folder only.

### Root conftest.py
- **File:** `conftest.py` (repo root)
- Added `collect_ignore_glob` to prevent collection of Mage `@test` functions as pytest test cases.

### C2 Experiment Results (Genuinely Executed)
- Ran `python -m iris_project.run_c2_experiments` on 2026-11-17.
- Results (Python 3.14.3, scikit-learn, 80/20 split, random_state=42):
  | max_depth | Test Accuracy | @test Gate | CSV Created |
  |-----------|--------------|------------|-------------|
  | 1 | 0.633 | FAILED | NO (gated) |
  | 2 | 0.967 | PASSED | YES |
  | 3 | 1.000 | PASSED | YES |
  | 4 | 1.000 | PASSED | YES |
  | 5 | 1.000 | PASSED | YES |

### Screenshots — Reference Material Notice
- All screenshots in `screenshots/` are inherited from the reference repository (Mansi Grover / mxnsi04).
- They are **not** Neelanjana's own execution evidence.
- They are retained as reference/structural material only.
- Neelanjana must replace them with her own screenshots after executing against her Snowflake account, RabbitMQ broker, and GitHub Actions.

---

## Original Implementation (Inherited from mxnsi04/freshcart-pipelines)
The following components were inherited without modification:
- `elt/freshcart_elt.ipynb` — full ELT notebook (Snowflake-dependent)
- `elt/pipeline_runner.py` — ELT orchestration (Bug 1 fixed by Neelanjana)
- `elt/run_b1_baseline.py`, `run_b3_currency.py`, `run_b4_scd2.py`, `run_b5_quality.py`
- `elt/trace_records.py`
- `iris_project/` — all Mage pipeline blocks (evaluate_model @test added by Neelanjana)
- `stream/dispatcher.py`, `stream/driver.py`, `stream/freshcart_consumer.py`
- `stream/run_bonus_experiment.py`, `stream/run_stream_test.py`
- `tests/test_prepare_data.py`, `tests/test_stream_routing.py`
- `.github/workflows/ci.yml`
- `.gitignore`, `.env.example`
- `report/part_*.md` files (content)
- All `screenshots/` images
