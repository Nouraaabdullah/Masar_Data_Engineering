# Lab 04 — Delta Reliability

## What Ran
Tested Delta corrections, conflicts, prior-version reads, atomic failure, schema evolution, compaction, restore, and VACUUM dry-run behaviour.

## Results
- Business rows remained 75 after correction.
- Delta version changed from 1 to 2.
- Same-revision conflicts were rejected.
- Previous versions were readable.
- Mixed valid/invalid batches were rejected atomically.
- Maintenance checks passed and trusted Silver remained unchanged.

## Evidence
- `Masar_All_Labs.ipynb`


## Interpretation
Delta provides controlled updates, transaction safety, history, and recovery without silently corrupting trusted business data.
