"""Candidate scoring check and top-candidate export.

This script works with the processed candidate table included in this
repository. It recomputes the baseline composite score from the stored score
components and rewrites the Top N table if requested.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

BASE_WEIGHTS = {
    "score_energy": 0.23,
    "score_cf": 0.14,
    "score_turbines": 0.18,
    "score_load_dist": 0.14,
    "score_town_dist": 0.10,
    "score_lowrisk": 0.10,
    "score_elevation": 0.06,
    "score_slope": 0.05,
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def recompute_score(df: pd.DataFrame) -> pd.Series:
    missing = [col for col in BASE_WEIGHTS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing score columns: {missing}")
    score = pd.Series(0.0, index=df.index)
    for column, weight in BASE_WEIGHTS.items():
        score = score + weight * pd.to_numeric(df[column], errors="coerce")
    return score


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/processed/hainan_candidate_points_with_constraints.csv")
    parser.add_argument("--output", default="data/processed/hainan_top10_candidates.csv")
    parser.add_argument("--top-n", type=int, default=10)
    args = parser.parse_args()

    root = repo_root()
    df = pd.read_csv(root / args.input, encoding="utf-8-sig")
    df["composite_score_recomputed"] = recompute_score(df)
    ranking_column = "composite_score_v4" if "composite_score_v4" in df.columns else "composite_score_recomputed"
    ranked = df.sort_values(ranking_column, ascending=False).reset_index(drop=True)
    ranked.head(args.top_n).to_csv(root / args.output, index=False, encoding="utf-8-sig")

    if "composite_score_v4" in df.columns:
        delta = (df["composite_score_recomputed"] - df["composite_score_v4"]).abs().max()
        print(f"max_abs_score_delta={delta:.6g}")
    print(ranked[["latitude", "longitude", ranking_column]].head(args.top_n).to_string(index=False))


if __name__ == "__main__":
    main()
