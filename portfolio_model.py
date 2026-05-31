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
        "evidence_artifacts": 5,
        "community_utility": 3,
        "technical_depth": 3,
        "focus_alignment": 4,
        "release_safety": 4,
        "profile_clarity": 3,
        "next_action": "Add a 10-minute reader path across the synthetic explanation reports.",
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


PROFILE_REFERENCES = [
    {
        "profile": "Andrej Karpathy",
        "url": "https://github.com/karpathy",
        "pattern": "flagship_clarity",
        "lesson": "A few memorable flagship repos can define a public technical identity.",
    },
    {
        "profile": "Sebastian Raschka",
        "url": "https://github.com/rasbt",
        "pattern": "teaching_asset",
        "lesson": "Book-linked, from-scratch material makes a repo useful beyond the author.",
    },
    {
        "profile": "Chip Huyen",
        "url": "https://github.com/chiphuyen",
        "pattern": "teaching_asset",
        "lesson": "Books, micro tools, and resource repos can reinforce one coherent AI-engineering identity.",
    },
    {
        "profile": "Francois Chollet",
        "url": "https://github.com/fchollet",
        "pattern": "research_artifact",
        "lesson": "A profile can connect frameworks, notebooks, benchmarks, and documentation.",
    },
    {
        "profile": "Jeremy Howard",
        "url": "https://github.com/jph00",
        "pattern": "notebook_to_software",
        "lesson": "Notebook-first workflows can still become maintained software and teaching assets.",
    },
    {
        "profile": "Jake VanderPlas",
        "url": "https://github.com/jakevdp",
        "pattern": "notebook_to_software",
        "lesson": "Open notebooks, tutorials, and libraries can serve as a durable learning surface.",
    },
    {
        "profile": "tiangolo",
        "url": "https://github.com/tiangolo",
        "pattern": "developer_experience",
        "lesson": "A family of tools can share one developer-experience promise.",
    },
    {
        "profile": "Armin Ronacher",
        "url": "https://github.com/mitsuhiko",
        "pattern": "minimal_infrastructure",
        "lesson": "Small, dependable infrastructure tools compound into long-term credibility.",
    },
    {
        "profile": "Hugging Face",
        "url": "https://github.com/huggingface",
        "pattern": "ecosystem_bridge",
        "lesson": "A public profile can act as a product/community map across many related tools.",
    },
    {
        "profile": "Hamel Husain",
        "url": "https://github.com/hamelsmu",
        "pattern": "evaluable_error_analysis",
        "lesson": "AI evals projects should expose error-analysis artifacts readers can inspect.",
    },
    {
        "profile": "Jason Liu",
        "url": "https://github.com/jxnl",
        "pattern": "practical_learning_surface",
        "lesson": "A profile can connect consulting, tutorials, talks, and reusable AI tooling.",
    },
    {
        "profile": "Christopher Olah",
        "url": "https://github.com/colah",
        "pattern": "explanation_gallery",
        "lesson": "Interpretability work becomes stronger when explanations are visual and inspectable.",
    },
    {
        "profile": "Been Kim",
        "url": "https://beenkim.github.io/",
        "pattern": "interpretability_evaluation",
        "lesson": "Explanation methods need explicit tests, counterexamples, and scope conditions.",
    },
]


PROFILE_PATTERN_WEIGHTS = {
    "flagship_clarity": 0.17,
    "evidence_trace": 0.17,
    "teaching_asset": 0.15,
    "developer_experience": 0.14,
    "notebook_to_software": 0.12,
    "ecosystem_bridge": 0.10,
    "minimal_infrastructure": 0.08,
    "release_boundary": 0.07,
}


PROJECT_PATTERN_COVERAGE = [
    {
        "project": "l40s-llm-bench",
        "flagship_clarity": 5,
        "evidence_trace": 5,
        "teaching_asset": 3,
        "developer_experience": 4,
        "notebook_to_software": 3,
        "ecosystem_bridge": 3,
        "minimal_infrastructure": 4,
        "release_boundary": 5,
    },
    {
        "project": "FaithfulRepair",
        "flagship_clarity": 4,
        "evidence_trace": 5,
        "teaching_asset": 2,
        "developer_experience": 2,
        "notebook_to_software": 2,
        "ecosystem_bridge": 3,
        "minimal_infrastructure": 2,
        "release_boundary": 3,
    },
    {
        "project": "arc-xai-reasoning",
        "flagship_clarity": 3,
        "evidence_trace": 5,
        "teaching_asset": 3,
        "developer_experience": 3,
        "notebook_to_software": 3,
        "ecosystem_bridge": 2,
        "minimal_infrastructure": 2,
        "release_boundary": 4,
    },
    {
        "project": "birdclef2026-xai",
        "flagship_clarity": 2,
        "evidence_trace": 4,
        "teaching_asset": 2,
        "developer_experience": 2,
        "notebook_to_software": 2,
        "ecosystem_bridge": 2,
        "minimal_infrastructure": 2,
        "release_boundary": 3,
    },
]


NEXT_EXPERIMENTS = {
    "l40s-llm-bench": "Add the first real vLLM smoke run when GPU/server access is ready.",
    "FaithfulRepair": "Add a synthetic end-to-end demo notebook that shows claim, citation, verifier signal, repair action, and limitation.",
    "arc-xai-reasoning": "Add a 10-minute reader path across logger, taxonomy, coverage, audit, and composition gallery.",
    "birdclef2026-xai": "Add a synthetic failure taxonomy report that explains false positives, weak evidence, and competition-safe boundaries.",
}


PROJECT_RELEASE_MULTIPLIERS = {
    "l40s-llm-bench": 1.40,
    "FaithfulRepair": 0.85,
    "arc-xai-reasoning": 0.85,
    "birdclef2026-xai": 0.55,
}


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


def pattern_gap_score(
    project: dict[str, Any],
    weights: dict[str, float] = PROFILE_PATTERN_WEIGHTS,
) -> float:
    return round(
        sum((5 - float(project[pattern])) * weight for pattern, weight in weights.items()),
        3,
    )


def project_pattern_gaps(
    project: dict[str, Any],
    weights: dict[str, float] = PROFILE_PATTERN_WEIGHTS,
    limit: int = 3,
) -> list[dict[str, Any]]:
    gaps = []
    for pattern, weight in weights.items():
        current = float(project[pattern])
        gaps.append(
            {
                "pattern": pattern,
                "current": current,
                "weighted_gap": round((5 - current) * weight, 3),
            }
        )
    return sorted(gaps, key=lambda row: row["weighted_gap"], reverse=True)[:limit]


def rank_optimization_opportunities(
    projects: list[dict[str, Any]] = PROJECT_PATTERN_COVERAGE,
) -> list[dict[str, Any]]:
    rows = []
    for project in projects:
        opportunity_score = pattern_gap_score(project)
        release_multiplier = PROJECT_RELEASE_MULTIPLIERS[project["project"]]
        rows.append(
            {
                "project": project["project"],
                "opportunity_score": opportunity_score,
                "release_multiplier": release_multiplier,
                "publish_priority": round(opportunity_score * release_multiplier, 3),
                "top_gaps": project_pattern_gaps(project),
                "next_experiment": NEXT_EXPERIMENTS[project["project"]],
            }
        )
    return sorted(rows, key=lambda row: row["publish_priority"], reverse=True)


def portfolio_report(rows: list[dict[str, Any]]) -> str:
    opportunities = rank_optimization_opportunities()
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
        "| Book/notebook bridge | Educational notebooks can become durable public assets | Add small synthetic notebooks only when they are safe to release |",
        "| Developer experience ecosystem | Related tools should share one promise | Give each repo a 10-minute path and consistent scripts |",
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
            "## Optimization Queue",
            "",
            "| Rank | Project | Gap score | Publish priority | Top gaps | Next experiment |",
            "|---|---|---|---|---|---|",
        ]
    )
    for index, row in enumerate(opportunities, start=1):
        top_gaps = ", ".join(gap["pattern"] for gap in row["top_gaps"])
        lines.append(
            f"| {index} | {row['project']} | {row['opportunity_score']} | "
            f"{row['publish_priority']} | {top_gaps} | {row['next_experiment']} |"
        )
    lines.extend(
        [
            "",
            "## Expanded Inspiration Sources",
            "",
            "| Profile | Pattern | Local lesson |",
            "|---|---|---|",
        ]
    )
    for reference in PROFILE_REFERENCES:
        lines.append(
            f"| [{reference['profile']}]({reference['url']}) | "
            f"{reference['pattern']} | {reference['lesson']} |"
        )
    lines.append("")
    return "\n".join(lines)


def write_json(path: str | Path, data: Any) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
