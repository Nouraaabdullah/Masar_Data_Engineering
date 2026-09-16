# Lab 05 — Kafka Streaming

## What Ran
Streamed GPS events through Kafka and Spark Structured Streaming into Delta using persistent checkpoints, then tested restart, replay, offsets, and late-event handling.

## Results
- Transport rows: [216, 216, 218, 219]
- Unique event IDs: [216, 216, 216, 217]
- Checkpoint files were present.
- Restart reused the same logical query identity.
- Kafka offsets reconciled successfully.
- Late event was retained.
- All streaming checks passed.

## Evidence
- `Masar_All_Labs.ipynb`
- `day04/STUDENT.ipynb`
- `outputs/day04_handoff.zip`

## Interpretation
Transport deliveries can repeat without creating duplicate logical events. Checkpoints allow the stream to restart safely and continue processing.
