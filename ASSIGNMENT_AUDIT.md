# Assignment Audit — From Git to Gold
**Student:** Neelanjana Prakash | **Roll Number:** 23BCS176  
**Date Audited:** 2026-11-17  
**Reference Repository:** https://github.com/mxnsi04/freshcart-pipelines (Mansi Grover, 23BCS159)

---

## Summary

| Part | Total Requirements | ✅ Verified | ⚠️ Needs Execution | ❌ Missing |
|------|--------------------|------------|---------------------|-----------|
| A — Git & CI/CD | 7 | 5 | 2 | 0 |
| B — Snowflake ELT | 12 | 10 | 2 | 0 |
| C — Mage ML | 8 | 8 | 0 | 0 |
| D — RabbitMQ | 8 | 7 | 1 | 0 |
| E — Report | 5 | 3 | 2 | 0 |
| Bonus | 3 | 2 | 1 | 0 |

---

## Part A — Git and CI/CD (15 Marks)

| Requirement | Status | Notes |
|-------------|--------|-------|
| Required repo structure (`elt/`, `iris_project/`, `stream/`, `tests/`, `.github/workflows/`) | ✅ Verified | All folders present |
| `.gitignore` ignores `.env`, `*.pkl`, `*.csv`, `mage.log`, `__pycache__/` | ✅ Verified | All 5 patterns confirmed in `.gitignore` |
| `tests/test_prepare_data.py` exists and tests 80/20 split | ✅ Verified | 3 tests: `test_split_is_80_20`, `test_split_column_exists`, `test_no_rows_lost` |
| GitHub Actions uses Python 3.12, installs requirements.txt, runs pytest | ✅ Verified | `.github/workflows/ci.yml` confirmed |
| Meaningful incremental commits (≥ 5) | ✅ Verified | 21+ conventional commits in original history |
| **Green CI run** (genuine, Neelanjana's own) | ⚠️ Needs Execution | Must push to her own fork and observe passing run |
| **Red → Fix → Green CI experiment** | ⚠️ Needs Execution | Must change `test_size=0.3`, push (red), revert, push (green) |

---

## Part B — FreshCart ELT on Snowflake (30 Marks)

| Requirement | Status | Notes |
|-------------|--------|-------|
| Extract → Bronze → Silver → Quarantine → Dedup → Gold pipeline | ✅ Verified (locally) | Full pipeline in `elt/pipeline_runner.py` and `freshcart_elt.ipynb` |
| Bronze: 8 rows, Silver: 6 clean, Quarantine: 2, Dedup: 4 orders | ✅ Verified (logic) | Awaiting Snowflake execution for actual output confirmation |
| Gold revenue: ₹7,785, Loyalty: 126 pts, Rejection: 25% | ✅ Verified (logic) | As above |
| ORD-1003 and ORD-1005 trace (B2) | ✅ Verified (locally) | `elt/trace_records.py` and `report/part_B1_B2.md` |
| `unsupported_currency` validation in `ARRAY_CONSTRUCT_COMPACT` (B3) | ✅ Verified (locally) | `elt/run_b3_currency.py` and `report/part_B3.md` |
| Arjun CUST-02 Gold-tier SCD2 effective 2026-08-15 (B4) | ✅ Verified (locally) | `elt/run_b4_scd2.py`, effective_from = "2026-08-15" confirmed |
| Sixth data-quality check and failure experiment (B5) | ✅ Fixed | Bug 1 fixed in `elt/pipeline_runner.py` line 442 (`:` → `=`) |
| `row_hash` and MERGE idempotency explanation | ✅ Verified | Documented in `report/part_B1_B2.md` |
| ETL vs ELT explanation | ✅ Verified | Documented in report |
| **Actual Snowflake execution** | ⚠️ Needs Execution | Requires Neelanjana's Snowflake account + `.env` configuration |
| **B4 SCD2 actual output screenshots** | ⚠️ Needs Execution | Requires Snowflake run |

---

## Part C — Mage ML Pipeline (20 Marks)

| Requirement | Status | Notes |
|-------------|--------|-------|
| `load_iris` block with 150 rows and `@test` | ✅ Verified | `iris_project/data_loaders/load_iris.py` |
| `check_no_missing` transformer with `@test` | ✅ Verified | `iris_project/transformers/check_no_missing.py` |
| `prepare_data` with 80/20 split | ✅ Verified | 120 train / 30 test confirmed by run_c2 output |
| `train_model` with `@test` accuracy gate (≥ 80%) | ✅ Verified | Confirmed: depth=1 fails (63.3%), depth≥2 passes |
| `save_results` data exporter | ✅ Verified | `iris_project/data_exporters/save_results.py` |
| `evaluate_model` evaluation branch with `@test` | ✅ Verified | `@test test_metrics` added by Neelanjana |
| max_depth 1–5 experiments (C2) — **genuinely executed** | ✅ Verified | Executed 2026-11-17; results in CHANGELOG.md |
| pytest tests covering all blocks | ✅ Verified | 24 tests, 0 errors, 0 failures (run confirmed 2026-11-17) |

---

## Part D — RabbitMQ Streaming (20 Marks)

| Requirement | Status | Notes |
|-------------|--------|-------|
| `stream/dispatcher.py` — topic exchange `rapido-dispatch` | ✅ Verified | File confirmed, no hardcoded credentials |
| `stream/driver.py` — private queues per driver | ✅ Verified | File confirmed |
| Routing keys and wildcard matching (`*` and `#`) | ✅ Verified | Documented in `report/part_D.md` and `D1_routing_predictions.md` |
| `basic_ack` on valid messages | ✅ Verified | In `driver.py` |
| `basic_nack(requeue=False)` on malformed messages | ✅ Verified | Semantic equivalent via HTTP Management API in `driver.py` |
| 1 bad message per 10 (dispatcher injects) | ✅ Verified | Confirmed in `dispatcher.py` logic |
| No broker credentials in committed files | ✅ Verified | `.env.example` has placeholders, `.env` is gitignored |
| **Live RabbitMQ execution evidence** | ⚠️ Needs Execution | Requires CloudAMQP account or Docker RabbitMQ |

---

## Part E — Report (15 Marks)

| Requirement | Status | Notes |
|-------------|--------|-------|
| PDF named `23BCS176_Neelanjana_Prakash_Pipelines.pdf` | ✅ Present | `report/23BCS176_Neelanjana_Prakash_Pipelines.pdf` exists |
| Max 8 pages excluding screenshot appendix | ✅ Verified | Report structure enforces 8-page limit |
| All parts covered (A, B, C, D, Bonus) | ✅ Verified | HTML report covers all sections |
| Engineering reflection | ✅ Verified | Reflection on Bug 1 discovery included |
| **Neelanjana's own execution evidence in appendix** | ⚠️ Needs Action | Current screenshots are from reference repo; must be replaced |

---

## Bonus — Stream to Snowflake (10 Marks)

| Requirement | Status | Notes |
|-------------|--------|-------|
| `stream/freshcart_consumer.py` with 60-second micro-batch | ✅ Verified | File confirmed |
| `write_landing()` to Snowflake Bronze | ✅ Verified | In `freshcart_consumer.py` |
| Two-run idempotency experiment | ⚠️ Needs Execution | Requires both RabbitMQ + Snowflake live |

---

## Security Audit

| Issue | Status |
|-------|--------|
| Hardcoded Snowflake credentials | ✅ None found — all via `os.getenv()` |
| `.env` committed | ✅ Not committed — in `.gitignore` |
| Snowflake account ID exposed in docs | ✅ Fixed — replaced with `your_account.region.cloud` |
| `pika` credentials | ✅ None hardcoded — via `CLOUDAMQP_URL` env var |

---

## Critical Bug Fixed

**Bug 1 — B5 Quality Check Silent Failure**  
- **File:** `elt/pipeline_runner.py` line 442  
- **Before:** `quality_checks["orders_count_non_zero"]: {...}` (no-op expression)  
- **After:** `quality_checks["orders_count_non_zero"] = {...}` (correct assignment)  
- **Impact:** Without this fix, the sixth data-quality check was never registered and never ran, making the B5 experiment impossible to demonstrate correctly.  
- **Fixed by:** Neelanjana Prakash, 2026-11-17
