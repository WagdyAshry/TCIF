# Results Directory

Empirical results reported in the paper (Section 6).

## Files

- `multi_seed_summary.json` — Aggregated metrics across 5 seeds
- `v18_metrics_seed42.json` — Per-seed test metrics (seed 42)
- `v18_metrics_seed123.json` — Per-seed test metrics (seed 123)
- `v18_metrics_seed456.json` — Per-seed test metrics (seed 456)
- `v18_metrics_seed789.json` — Per-seed test metrics (seed 789)
- `v18_metrics_seed2024.json` — Per-seed test metrics (seed 2024)
- `training_log_seed42.json` — Training history for seed 42

## Key Metrics (Test Set, Mean ± Std across 5 seeds)

| Metric | Value |
|---|---|
| RMSE (all horizons) | 0.0935 ± 0.0011 |
| DAS macro F1 | 0.3629 ± 0.0071 |
| Severity-weighted F1 | 0.3134 ± 0.0080 |
| Severe-class recall | 0.3441 ± 0.0256 |

## Per-Category F1 (Test Set, Mean ± Std)

| Category | F1 |
|---|---|
| Executive Escalation | 0.3017 ± 0.0074 |
| Supplier Escalation | 0.1102 ± 0.0371 |
| Budget Reallocation | 0.2680 ± 0.0464 |
| Monitoring Flag | 0.3209 ± 0.0244 |
| Routine Variance | 0.5506 ± 0.0039 |
| No Action | 0.6263 ± 0.0090 |
