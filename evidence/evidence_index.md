# Evidence Index — From Git to Gold
**Student:** Neelanjana Prakash | **Roll Number:** 23BCS176  
**Updated:** 2026-11-17  
**Reference Repository:** https://github.com/mxnsi04/freshcart-pipelines (Mansi Grover, 23BCS159)

> **Important:** All screenshots currently in `screenshots/` are inherited from the reference repository and represent Mansi Grover's execution. They are retained as structural reference material only. Neelanjana must replace them with her own screenshots after executing against her own accounts.

---

## Screenshot Status

| Screenshot File | Inherited? | Needs Replacement? |
|----------------|-----------|-------------------|
| `screenshots/part_A/A1_github_repo_page.png` | ✅ Yes | ⚠️ Yes — must show Neelanjana's own fork |
| `screenshots/part_A/A1_local_structure.png` | ✅ Yes | ⚠️ Yes — take new terminal screenshot |
| `screenshots/part_A/A3_github_actions_green.png` | ✅ Yes | ⚠️ Yes — from Neelanjana's own CI run |
| `screenshots/part_A/A3_github_actions_red.png` | ✅ Yes | ⚠️ Yes — from Neelanjana's own CI fail run |
| `screenshots/part_A/A3_github_actions_fixed_green.png` | ✅ Yes | ⚠️ Yes — from Neelanjana's own CI fix run |
| `screenshots/part_A/A3_github_actions_history_overview.png` | ✅ Yes | ⚠️ Yes — from Neelanjana's own Actions history |
| `screenshots/part_B/B1_baseline_tables_verification.png` | ✅ Yes | ⚠️ Yes — Neelanjana's Snowflake output |
| `screenshots/part_B/B2_record_trace_ord1003_ord1005.png` | ✅ Yes | ⚠️ Yes — Neelanjana's Snowflake trace |
| `screenshots/part_B/B3_unsupported_currency_before_after.png` | ✅ Yes | ⚠️ Yes — Neelanjana's Snowflake |
| `screenshots/part_B/B4_scd2_arjun_gold_update.png` | ✅ Yes | ⚠️ Yes — Neelanjana's Snowflake |
| `screenshots/part_B/B5_quality_check_normal_and_failure.png` | ✅ Yes | ⚠️ Yes — Neelanjana's Snowflake |
| `screenshots/part_C/C1_C3_mage_pipeline_evidence.png` | ✅ Yes | ⚠️ Yes — Neelanjana's terminal run |
| `screenshots/part_C/C2_experiment_terminal_output.png` | ✅ Yes | ⚠️ Yes — Neelanjana's C2 experiment (can use run_c2_experiments.py output) |
| `screenshots/part_C/C4_github_ci_passed.png` | ✅ Yes | ⚠️ Yes — from Neelanjana's CI run |
| `screenshots/part_D/D1_routing_predictions_verified.png` | ✅ Yes | ⚠️ Yes — Neelanjana's RabbitMQ |
| `screenshots/part_D/D2_D3_stream_terminal_output.png` | ✅ Yes | ⚠️ Yes — Neelanjana's RabbitMQ |
| `screenshots/part_E/01_final_report_cover.png` | ✅ Yes | ⚠️ Yes — Neelanjana's PDF cover |
| `screenshots/part_E/02_report_page_count_proof.png` | ✅ Yes | ⚠️ Yes — Neelanjana's PDF |
| `screenshots/part_E/03_integration_architecture_diagram.png` | ✅ Yes | ⚠️ Optional |
| `screenshots/part_E/04_viva_preparation_document.png` | ✅ Yes | ⚠️ Optional |
| `screenshots/bonus/01_rabbitmq_consumer_batch_collection.png` | ✅ Yes | ⚠️ Yes — Neelanjana's execution |
| `screenshots/bonus/02_landing_file_and_snowflake_load.png` | ✅ Yes | ⚠️ Yes — Neelanjana's Snowflake |
| `screenshots/bonus/03_gold_first_batch_vs_replay_idempotency.png` | ✅ Yes | ⚠️ Yes — Neelanjana's Snowflake |

---

## Locally Executed Evidence (Genuine)

### C2 Experiment — Executed 2026-11-17 on Neelanjana's machine
```
python -m iris_project.run_c2_experiments
Platform: Python 3.14.3 | scikit-learn | 80/20 split (random_state=42)

max_depth=1 | Accuracy=0.633 | @test FAILED | CSV: NOT created (quality gate blocked)
max_depth=2 | Accuracy=0.967 | @test PASSED | CSV: created (30 predictions)
max_depth=3 | Accuracy=1.000 | @test PASSED | CSV: created (30 predictions)
max_depth=4 | Accuracy=1.000 | @test PASSED | CSV: created (30 predictions)
max_depth=5 | Accuracy=1.000 | @test PASSED | CSV: created (30 predictions)
```

### pytest Test Suite — Executed 2026-11-17 on Neelanjana's machine
```
python -m pytest tests/ -v
Platform: Python 3.14.3 | pytest 9.2.0

24 tests collected, 24 passed, 0 errors, 0 failures
Tests:
  test_check_no_missing.py      5 passed
  test_evaluate_model.py        4 passed
  test_prepare_data.py          3 passed
  test_stream_routing.py        6 passed
  test_train_model.py           6 passed
```

---

## Screenshots Neelanjana Must Capture

### Priority 1 — Part A (CI/CD)
1. **A1 — Repository structure**: Open terminal in repo root, run `tree /f` or show folder structure. Screenshot the terminal.
2. **A3 — Green CI run**: After pushing to your fork, go to GitHub → Actions → your passing run. Screenshot the green checkmark.
3. **A3 — Red CI run**: Change `test_size=0.3` in `iris_project/transformers/prepare_data.py`, commit, push. Screenshot the failing run.
4. **A3 — Fix CI run**: Revert to `test_size=0.2`, commit, push. Screenshot the green run.
5. **A3 — CI history**: Screenshot the full Actions history showing 3 runs (green, red, green).

### Priority 2 — Part C (ML Pipeline)
6. **C2 — Terminal output**: Run `python -m iris_project.run_c2_experiments`. Screenshot the full terminal output showing all 5 depth results.
7. **C4 — pytest passing**: Run `python -m pytest tests/ -v`. Screenshot showing 24 passed.

### Priority 3 — Part B (Snowflake)
8. **B1 — Baseline tables**: Run `python -m elt.run_b1_baseline` with Snowflake configured. Screenshot the terminal output showing 8 bronze, 6 silver, 2 quarantine, 4 dedup, ₹7785 revenue.
9. **B2 — ORD-1003 / ORD-1005 trace**: Screenshot Snowflake output from `python -m elt.trace_records`.
10. **B3 — Currency validation**: Screenshot before/after adding unsupported_currency check.
11. **B4 — SCD2 Arjun**: Screenshot Snowflake `dim.customers_scd2` showing both rows for CUST-02 (Arjun) with `effective_from=2026-08-15`.
12. **B5 — Quality check failure**: Screenshot the quality check pipeline with 6th check passing and then failing with mock order.

### Priority 4 — Part D (RabbitMQ)
13. **D2/D3 — Live stream**: Run dispatcher.py and driver.py against CloudAMQP or Docker RabbitMQ. Screenshot the terminal showing routing, ACK and NACK.

### Priority 5 — Part E (Report)
14. **Report cover**: Open `report/23BCS176_Neelanjana_Prakash_Pipelines.pdf`. Screenshot page 1.
15. **Page count**: Screenshot the PDF with page count visible.

### Priority 6 — Bonus
16. **Bonus consumer**: Screenshot the micro-batch consumer running.
17. **Idempotency**: Screenshot Snowflake Gold table after Run 1 and Run 2 (same row count).

---

## Execution Logs

Genuine logs from Neelanjana's execution are in `evidence/execution_logs/`.

| Log File | Contents | Status |
|----------|----------|--------|
| `execution_logs/stream_execution.log` | Reference log from original run | Inherited |
| `execution_logs/bonus_experiment.log` | Reference log from original run | Inherited |
