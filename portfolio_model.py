from __future__ import annotations

import json
from pathlib import Path
from typing import Any


WEIGHTS = {
    "reproducibility": 0.20,
    "evidence_artifacts": 0.18,
    "community_utility": 0.17,
    "technical_depth": 0.15,
    "focus_alignment": 0.12,
    "release_safety": 0.10,
    "profile_clarity": 0.08,
}


PROJECTS = [
    {
        "project": "l40s-llm-bench",
        "status": "public GitHub repo",
        "reproducibility": 5,
        "evidence_artifacts": 5,
        "community_utility": 4,
        "technical_depth": 4,
        "focus_alignment": 4,
        "release_safety": 5,
        "profile_clarity": 4,
        "next_action": "Add first real vLLM smoke run when GPU/server access is ready.",
    },
    {
        "project": "FaithfulRepair",
        "status": "local public-safe shell",
        "reproducibility": 4,
        "evidence_artifacts": 5,
        "community_utility": 4,
        "technical_depth": 5,
        "focus_alignment": 5,
        "release_safety": 3,
        "profile_clarity": 3,
        "next_action": "Keep public package synthetic until manuscript/preprint strategy is stable.",
    },
    {
        "project": "arc-xai-reasoning",
        "status": "local public-safe shell",
        "reproducibility": 4,
        "evidence_artifacts": 4,
        "community_utility": 3,
        "technical_depth": 3,
        "focus_alignment": 4,
        "release_safety": 4,
        "profile_clarity": 3,
        "next_action": "Add public-safe rule composition toy cases before release.",
    },
    {
        "project": "birdclef2026-xai",
        "status": "local competition-safe shell",
        "reproducibility": 4,
        "evidence_artifacts": 4,
        "community_utility": 3,
        "technical_depth": 3,
        "focus_alignment": 3,
        "release_safety": 3,
        "profile_clarity": 3,
        "next_action": "Keep real notebooks private; add synthetic failure taxonomy only.",
    },
]


def score_project(project: dict[str, Any], weights: dict[str, float] = WEIGHTS) -> float:
    return round(
        sum(float(project[metric]) * weight for metric, weight in weights.items()),
        3,
    )


def rank_projects(projects: list[dict[str, Any]] = PROJECTS) -> list[dict[str, Any]]:
    rows = []
    for project in projects:
        rows.append({**project, "score": score_project(project)})
    return sorted(rows, key=lambda row: row["score"], reverse=True)


def portfolio_report(rows: list[dict[str, Any]]) -> str:
    lines = [
        "# GitHub Portfolio Signal Model",
        "",
        "This model converts profile/repo presentation lessons from strong GitHub",
        "AI builders into a small prioritization score. Scores are local planning",
        "signals, not claims about research quality.",
        "",
        "## Inspiration Patterns",
        "",
        "| Pattern | Borrowed idea | Local translation |",
        "|---|---|---|",
        "| Strong flagship repos | A small number of memorable repos beats many vague repos | Keep `l40s-llm-bench` as the public flagship |",
        "| From-scratch educational clarity | Explain what the repo teaches or proves | Make every shell repo state its evidence boundary |",
        "| Implementation matrix | Consistent naming and README structure scale across many repos | Use repeatable docs: queue, checklist, report, scope note |",
        "| Infrastructure credibility | Benchmarks, manifests, and reproducibility artifacts matter | Prioritize raw logs, reports, tests, and run manifests |",
        "| Extended README index | Profile README can compensate for limited pinned slots | Add a concise project matrix and next-action table |",
        "",
        "## Weights",
        "",
        "| Metric | Weight |",
        "|---|---|",
    ]
    for metric, weight in WEIGHTS.items():
        lines.append(f"| {metric} | {weight} |")
    lines.extend(
        [
            "",
            "## Project Ranking",
            "",
            "| Rank | Project | Score | Status | Next action |",
            "|---|---|---|---|---|",
        ]
    )
    for index, row in enumerate(rows, start=1):
        lines.append(
            f"| {index} | {row['project']} | {row['score']} | "
            f"{row['status']} | {row['next_action']} |"
        )
    lines.extend(
        [
            "",
            "## Release Logic",
            "",
            "- Publish or pin only projects with clear evidence artifacts and low release risk.",
            "- Keep paper-sensitive and competition-sensitive repos as public-safe shells until their human gates clear.",
            "- Prefer one strong flagship plus a small set of explainable supporting projects.",
            "- Every public repo should show what it proves, how to reproduce it, and what it does not prove.",
            "",
        ]
    )
    return "\n".join(lines)


def write_json(path: str | Path, data: Any) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
