from portfolio_model import PROJECTS, rank_projects, score_project


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
