# Benchmark Evidence

## Cost Model

The cost model uses hypothetical teaching units (TU), not real currency.

Observed base scenario:

- Always-on total: **1460.00 TU**
- Scheduled total: **185.00 TU**
- Difference: **1275.00 TU**
- Break-even workload: **23.25 hours/day**

The scheduled strategy was cheaper under the selected low-utilization assumptions, but the advantage disappears at the break-even point.

## Spark Scan Benchmark

Both reads returned the same business result:

- Rows: **72**
- Non-null fares: **72**
- Total fare: **SAR 1794.60**

Observed local measurements:

| Format | Median |
|---|---:|
| CSV | 0.03394 s |
| Delta v0 | 0.19280 s |

The benchmark used one warm-up and four measured repetitions.

## Interpretation

CSV was faster in this specific small local run. This does not prove that CSV is generally faster than Delta in production.

The dataset is very small, and local OS/JVM/cache effects can influence timing.

Delta is used in this project primarily for reliability features such as ACID transactions, MERGE, schema enforcement, history and time travel.

## Evidence

- `Masar_All_Labs.ipynb`
- `reports/benchmark.json`
- `reports/plans/csv.txt`
- `reports/plans/delta_v0.txt`
