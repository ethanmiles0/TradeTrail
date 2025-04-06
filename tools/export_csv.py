from pathlib import Path
import csv
import json


def export_jsonl_to_csv(jsonl: Path, csv_out: Path) -> None:
    rows = []
    if Path(jsonl).exists():
        with Path(jsonl).open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                rows.append(json.loads(line))
    fields = [
        "id",
        "timestamp",
        "market",
        "side",
        "size",
        "price",
        "tags",
        "note",
    ]
    csv_out.parent.mkdir(parents=True, exist_ok=True)
    with Path(csv_out).open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            r = dict(r)
            r["tags"] = ",".join(r.get("tags", []))
            w.writerow(r)


if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("jsonl")
    p.add_argument("csv")
    a = p.parse_args()
    export_jsonl_to_csv(Path(a.jsonl), Path(a.csv))

