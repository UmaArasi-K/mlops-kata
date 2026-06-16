# mlops-kata

A disciplined, 12-week MLOps upskilling journey — from Python fundamentals to production-grade ML pipelines.

## What This Repo Tracks

Every day, one learning session, one code commit, one LeetCode problem. No shortcuts, no skipped days. Each week builds on the last, and the streak log holds me accountable.

This repo contains:
- **Daily code files** organized by week (`week-1/`, `week-2/`, etc.) — each file is a small, self-contained project targeting a specific concept
- **Streak log** (`streaks/log.md`) — honest daily record of what was built, what was solved, and how it went
- **Portfolio projects** — end-to-end pipelines that grow in complexity as the weeks progress, starting from Python+SQL and scaling to containerized ML services

## Tech Stack Being Built

| Week(s) | Focus | Tools |
|---------|-------|-------|
| 1–2 | Python + SQL foundations | Python, SQLite, pytest |
| 3–4 | Deep learning fundamentals | PyTorch, NumPy, Pandas |
| 5–6 | Containerization & APIs | Docker, FastAPI |
| 7–8 | Orchestration & pipelines | Airflow, MLflow |
| 9–10 | Infrastructure & deployment | Kubernetes, Helm |
| 11–12 | Integration & capstone | Full stack — ingest to serving |

## 12-Week Structure

**Phase 1 (Weeks 1–2):** Python and SQL — data structures, OOP, file I/O, JOINs, window functions, error handling. Everything downstream depends on this being solid.

**Phase 2 (Weeks 3–4):** PyTorch — tensors, autograd, training loops, basic model architectures. Hands-on, not theoretical.

**Phase 3 (Weeks 5–6):** Docker + FastAPI — containerizing models, building prediction endpoints, writing Dockerfiles that actually work in CI.

**Phase 4 (Weeks 7–8):** Airflow + MLflow — orchestrating training pipelines, tracking experiments, scheduling retraining jobs.

**Phase 5 (Weeks 9–10):** Kubernetes — deploying models to a cluster, health checks, scaling, Helm charts.

**Phase 6 (Weeks 11–12):** Capstone — a complete ML pipeline from data ingestion to model serving, integrating everything from the previous 10 weeks into one working system.

## How It Works

- **Weekdays:** 90 min learning + 45 min coding + 45 min LeetCode. Each session has a concrete deliverable committed to this repo.
- **Weekends:** Optional capstone/exploration time. No pressure, no guilt.
- **Fridays:** Weekly wrap — what was planned vs. what actually happened, skill delta, gaps carried forward.
- **Streak tracking:** Every day's work is logged in `streaks/log.md` with the topic, LeetCode problem, and self-rating.

## Running the Code

```bash
# Most files are standalone Python scripts
python week-1/day1_chunk1_unique_visitors.py

# For SQL-based files, sqlite3 is used inline — no external DB needed
python week-1/day3_chunk1_select_where.py
```

## CI

A GitHub Actions workflow runs on every push to `main`:
- Lints all Python files with `flake8`
- Verifies `streaks/log.md` exists (streak must not be deleted)
