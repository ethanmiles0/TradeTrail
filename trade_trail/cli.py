import argparse
import sys
import uuid
from datetime import datetime
from pathlib import Path

from .model import TradeEntry
from .store import JsonlStore


def _default_db() -> Path:
    return Path.cwd() / ".trade_trail" / "journal.jsonl"


def cmd_add(args: argparse.Namespace) -> int:
    store = JsonlStore(Path(args.db))
    entry = TradeEntry(
        id=str(uuid.uuid4()),
        timestamp=datetime.fromisoformat(args.time) if args.time else datetime.now(),
        market=args.market,
        side=args.side,
        size=float(args.size),
        price=float(args.price),
        tags=[t for t in (args.tags or []) if t],
        note=args.note,
    )
    store.append(entry.to_dict())
    print(entry.id)
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    store = JsonlStore(Path(args.db))
    rows = store.read_all()
    for r in rows:
        print(
            f"{r.get('timestamp')} {r.get('market'):8} {r.get('side'):4} "
            f"size={r.get('size')} price={r.get('price')} tags={','.join(r.get('tags', []))}"
        )
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="trade-trail", description="Tiny trade journal helper")
    p.add_argument("--db", default=str(_default_db()), help="Path to JSONL store")

    sub = p.add_subparsers(dest="cmd", required=True)

    add = sub.add_parser("add", help="Append a trade entry")
    add.add_argument("market")
    add.add_argument("side", choices=["buy", "sell"]) 
    add.add_argument("size")
    add.add_argument("price")
    add.add_argument("--tags", nargs="*", default=[])
    add.add_argument("--time", help="ISO timestamp; default now")
    add.add_argument("--note", default=None)
    add.set_defaults(func=cmd_add)

    ls = sub.add_parser("list", help="List stored entries")
    ls.set_defaults(func=cmd_list)

    return p


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

