from portfolio_model import (
    PROFILE_PATTERN_WEIGHTS,
    PROJECTS,
    PROJECT_PATTERN_COVERAGE,
    pattern_gap_score,
    rank_optimization_opportunities,
    rank_projects,
    score_project,
)


def test_score_project_uses_weighted_metrics() -> None:
    project = {metric: 5 for metric in PROJECTS[0] if metric not in {"project", "status", "next_action"}}

    assert score_project(project) == 5.0


def test_rank_projects_puts_flagship_first() -> None:
    rows = rank_projects()

    assert rows[0]["project"] == "l40s-llm-bench"
    assert rows[0]["score"] > rows[-1]["score"]


def test_project_scores_have_next_actions() -> None:
    rows = rank_projects()

    assert all(row["next_action"] for row in rows)
    assert all(0 <= row["score"] <= 5 for row in rows)


def test_pattern_gap_score_rewards_missing_patterns() -> None:
    complete = {
        "project": "complete",
        **{pattern: 5 for pattern in PROFILE_PATTERN_WEIGHTS},
    }
    first_project = PROJECT_PATTERN_COVERAGE[0]

    assert pattern_gap_score(complete) == 0
    assert pattern_gap_score(first_project) > 0


def test_optimization_queue_has_actionable_gaps() -> None:
    rows = rank_optimization_opportunities()

    assert rows[0]["publish_priority"] >= rows[-1]["publish_priority"]
    assert rows[0]["project"] == "l40s-llm-bench"
    assert all(row["top_gaps"] for row in rows)
    assert all(row["next_experiment"] for row in rows)
