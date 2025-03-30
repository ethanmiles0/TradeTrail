# TradeTrail

Solo project to experiment with simple, local-first trade journaling utilities. The idea is to keep a lightweight record of trades, notes, and tags, and export quick summaries.

This repository evolves incrementally like a weekend/evening hobby project.

## Rough roadmap
- Minimal data model for entries
- Append-only JSONL store
- Tiny CLI to add/list/export
- Basic filters: date, market, tag
- CSV export for spreadsheets

No runtime guarantees; code may be rough while iterating.

## Usage (CLI)
Example adding an entry:

```
python -m trade_trail.cli add BTC-USD buy 0.1 62000 --tags swing log --note "broke out on HTF"
```

List entries:

```
python -m trade_trail.cli list
```
