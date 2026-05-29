"""Inspect the forecasting metric summary table."""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/processed/forecasting_metrics.csv")
    args = parser.parse_args()

    df = pd.read_csv(repo_root() / args.input, encoding="utf-8-sig")
    required = {"site_type", "horizon", "model", "mae_kw", "rmse_kw", "nmae_percent", "nrmse_percent"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing forecasting metric columns: {sorted(missing)}")
    best = df.sort_values("nrmse_percent").groupby(["site_type", "horizon"], as_index=False).first()
    print(best[["site_type", "horizon", "model", "nmae_percent", "nrmse_percent"]].to_string(index=False))


if __name__ == "__main__":
    main()
