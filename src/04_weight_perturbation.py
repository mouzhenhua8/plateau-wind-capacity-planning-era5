"""Weight-perturbation ranking diagnostic for the candidate table."""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

BASE_WEIGHTS = {
    "w_energy": 0.23,
    "w_cf": 0.14,
    "w_turbines": 0.18,
    "w_load": 0.14,
    "w_town": 0.10,
    "w_lowrisk": 0.10,
    "w_elev": 0.06,
    "w_slope": 0.05,
}

SCORE_COLUMNS = {
    "w_energy": "score_energy",
    "w_cf": "score_cf",
    "w_turbines": "score_turbines",
    "w_load": "score_load_dist",
    "w_town": "score_town_dist",
    "w_lowrisk": "score_lowrisk",
    "w_elev": "score_elevation",
    "w_slope": "score_slope",
}

GROUPS = {
    "Baseline": [],
    "Resource+": ["w_energy", "w_cf"],
    "Resource-": ["w_energy", "w_cf"],
    "Configuration+": ["w_turbines"],
    "Configuration-": ["w_turbines"],
    "Location+": ["w_load", "w_town"],
    "Location-": ["w_load", "w_town"],
    "Constraint+": ["w_lowrisk", "w_elev", "w_slope"],
    "Constraint-": ["w_lowrisk", "w_elev", "w_slope"],
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def scenario_weights(name: str) -> dict[str, float]:
    weights = BASE_WEIGHTS.copy()
    factor = 1.2 if name.endswith("+") else 0.8 if name.endswith("-") else 1.0
    for key in GROUPS[name]:
        weights[key] *= factor
    total = sum(weights.values())
    return {key: value / total for key, value in weights.items()}


def score(df: pd.DataFrame, weights: dict[str, float]) -> pd.Series:
    missing = [col for col in SCORE_COLUMNS.values() if col not in df.columns]
    if missing:
        raise ValueError(f"Missing score columns: {missing}")
    out = pd.Series(0.0, index=df.index)
    for weight_key, column in SCORE_COLUMNS.items():
        out = out + weights[weight_key] * pd.to_numeric(df[column], errors="coerce")
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/processed/hainan_candidate_points_with_constraints.csv")
    parser.add_argument("--output", default="")
    args = parser.parse_args()

    root = repo_root()
    df = pd.read_csv(root / args.input, encoding="utf-8-sig")
    rows = []
    for scenario in GROUPS:
        tmp = df.copy()
        tmp["score"] = score(tmp, scenario_weights(scenario))
        tmp = tmp.sort_values("score", ascending=False).reset_index(drop=True)
        best = tmp.iloc[0]
        rows.append({
            "scenario": scenario,
            "top_latitude": best["latitude"],
            "top_longitude": best["longitude"],
            "top_score": best["score"],
        })
    summary = pd.DataFrame(rows)
    if args.output:
        summary.to_csv(root / args.output, index=False, encoding="utf-8-sig")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
