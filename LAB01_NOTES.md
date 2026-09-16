# Lab 01 — Bronze Ingestion

## What Ran
Inspected the source data, validated the manifest, then ingested Trips, Drivers, and GPS Events into append-only Delta Bronze tables. The Trips feed was replayed to test duplicate delivery handling.

## Results
- Source: 72 trips, 6 drivers, 216 GPS events.
- 10 city values required normalization.
- After replay: Bronze Trips = 144 rows while business trips remained 72.
- All Bronze validation checks passed.

## Evidence
- `Masar_All_Labs.ipynb`

## Interpretation
Bronze preserves raw delivery history, including repeated deliveries. Deduplication and normalization are handled later in Silver.
