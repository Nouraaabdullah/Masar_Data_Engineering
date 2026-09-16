# Lab 02 — Cost and Performance Evidence

## What Ran
Compared always-on and scheduled compute using hypothetical teaching units, then benchmarked equal-result CSV and Delta reads using Spark.

## Results
- Always-on total: 1460 TU
- Scheduled total: 185 TU
- Break-even workload: 23.25 hours/day
- CSV median: 0.03394 s
- Delta v0 median: 0.19280 s
- Both scans returned 72 rows and total fare SAR 1794.60.

## Evidence
- `Masar_All_Labs.ipynb`


## Interpretation
Scheduled compute was cheaper under the selected assumptions. The local benchmark does not prove general production performance because the dataset is small and caching may affect results.
