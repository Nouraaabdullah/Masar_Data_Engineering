# Lab 01 — Bronze Ingestion and Source Quality

## Identity

- **Lab:** Lab 01 — Real Delta Bronze
- **Project:** Masar Mini-Lakehouse
- **Dataset:** `MASAR_SMALL_V1`
- **Primary execution evidence:** [`Masar_All_Labs.ipynb`](./Masar_All_Labs.ipynb)
- **Daily source notebook:** [`day01/STUDENT.ipynb`](./day01/STUDENT.ipynb)
- **Repository branch:** `main`
- **Execution notebook version reviewed:** `aa26394b`
- **Environment:** Python 3.11.16, Java 17, PySpark 3.5.8, Delta Lake 3.3.3
- **Execution period:** September 2026; exact cell execution timestamps are retained in the notebook metadata.
- **Manifest verification:** 10 manifest files were verified successfully.
- **Manifest hash:** The retained notebook output does not print a single manifest hash, so no hash is claimed here.

---

## What Ran

Lab 01 first inspected the fixed synthetic Masar source dataset before writing any Bronze tables.

The following source feeds were loaded and validated:

- Trips CSV
- Drivers CSV
- GPS events NDJSON

The source-inspection stage checked:

- Record counts
- Key uniqueness
- Missing top-level fields
- Referential relationships
- GPS coordinates
- City-label consistency

After source inspection, the native Bronze pipeline was executed using Spark and Delta Lake.

The Bronze pipeline:

1. Loaded the original trips, drivers, and GPS feeds.
2. Wrote each feed to an append-only Delta Bronze table.
3. Added ingestion and source-lineage metadata.
4. Replayed the trips feed as a second delivery.
5. Verified that the replay was preserved in Bronze.
6. Verified that the underlying storage contained real Delta files.

The final retained execution shows a successful run for these sections.

---

## Observed Source Evidence

The fixed dataset contained:

| Feed | Observed rows |
|---|---:|
| Trips | 72 |
| Drivers | 6 |
| GPS events | 216 |

Source profiling showed:

- Trips duplicate key groups: `0`
- Drivers duplicate key groups: `0`
- GPS event duplicate key groups: `0`
- Trips without a matching driver: `0`
- GPS events without a matching trip: `0`
- GPS events with invalid coordinates: `0`

No missing top-level fields were reported for the three base feeds.

The source-inspection checks all passed:

```text
source_counts = true
unique_base_keys = true
base_top_level_complete = true
valid_links_and_coordinates = true
three_events_per_trip = true
base_city_set = true
