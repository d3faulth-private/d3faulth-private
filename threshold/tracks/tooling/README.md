# Quiet Signal / Tool development

**Assessment 01 · Deterministic audit-log analysis**

Build a command-line tool in your preferred language that reads `evidence/events.jsonl` and writes one JSON report. The records are fictional, out of order, and contain deliberate noise. No networking is needed.

## Required behavior

1. Read lines in file order. A valid record is a JSON object containing nonempty string values for `event_id`, `at`, `account`, `source_ip`, `outcome`, and `kind`. `at` must be an ISO 8601 timestamp with an explicit timezone; `source_ip` must be a valid IPv4 or IPv6 address; `outcome` must be `success` or `failure`; `kind` must be `auth` or `file`. Extra fields are allowed. Invalid lines, including blank lines, are recorded using **one-based** line numbers and skipped.
2. Deduplicate valid records by `event_id`: **the first valid occurrence in file order wins**, even when a later duplicate contains conflicting values. Record skipped duplicates by their one-based line numbers. Invalid lines do not reserve an ID.
3. Analyze only `auth` records. For each successful authentication at time `T`, find failed authentications for the **same account and source IP** in **[T − 300 seconds, T)**. Include a failure exactly five minutes earlier; exclude one at exactly `T`. Compare timezone-normalized instants.
4. Emit an alert if there are at least three distinct matching failure events. Include every qualifying failure, sorted by UTC timestamp then event ID. Sort alerts by success UTC timestamp then success event ID. A failure can contribute to more than one success window.
5. The report has exactly `alerts`, `invalid_lines`, and `duplicate_lines`. Each alert has exactly `account`, `source_ip`, `success_event`, `success_utc`, and `failure_events`. Format UTC instants as `YYYY-MM-DDTHH:MM:SSZ`. List invalid/duplicate line numbers in ascending order. See `answer.example.json` for the output shape.

This fixture contains whole-second timestamps and canonical IP spellings. Equal IPs mean equal parsed addresses. Your implementation must not depend on the fixture's exact IDs or line count.

## Deliverables

- Your analyzer source, how to run it, and its generated report as `answer.json`.
- Tests for out-of-order records, timezone offsets, duplicate conflicts, the inclusive/exclusive time boundaries, and a clean input with no alerts.
- A brief explanation of the algorithm and memory/runtime behavior as the input grows.

From the repository root, check the report:

```sh
python3 threshold/verify.py tooling /path/to/answer.json
```

The local checker validates only the supplied fixture's report. Review also examines your source and tests, and uses a changed input.

[All tracks](../../README.md)
