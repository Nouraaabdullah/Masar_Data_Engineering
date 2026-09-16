# Lab 03 — Staging and Incremental Silver

## What Ran
Converted Bronze data into typed staging tables, built incremental Silver, tested replay and late-arriving data, and validated the same transformations with dbt.

## Results
- Staging: 144 trips, 6 drivers, 216 GPS events.
- Silver business keys were unique.
- Replays preserved business content.
- Late records were retained.
- Base/rerun: 72 rows, SAR 1794.60.
- Late/late replay: 75 rows, SAR 1875.60.
- dbt status: `PASSED_DBT_NATIVE`.

## Evidence
- `Masar_All_Labs.ipynb`


## Interpretation
Silver converts repeated Bronze deliveries into a stable trusted business state. Re-running the same data does not create duplicates, while genuine late records are retained.
