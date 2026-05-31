from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from portfolio_model import (
    portfolio_report,
    rank_optimization_opportunities,
    rank_projects,
    write_json,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-output", default="outputs/portfolio_signal_model.json")
    parser.add_argument("--opportunities-output", default="outputs/profile_optimization_queue.json")
    parser.add_argument("--report", default="outputs/portfolio_signal_model.md")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = rank_projects()
    opportunities = rank_optimization_opportunities()
    write_json(args.json_output, rows)
    write_json(args.opportunities_output, opportunities)
    report = Path(args.report)
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(portfolio_report(rows), encoding="utf-8")
    print(f"wrote portfolio scores to {args.json_output}")
    print(f"wrote optimization queue to {args.opportunities_output}")
    print(f"wrote portfolio report to {args.report}")


if __name__ == "__main__":
    main()
