"""Summarize density-corrected candidate results.

The repository includes processed density-corrected outputs. Raw ERA5 hourly
files are not redistributed here; recomputing the hourly density correction
requires downloading ERA5 data separately from the Copernicus Climate Data Store.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/processed/density_corrected_results.csv")
    parser.add_argument("--top-n", type=int, default=10)
    args = parser.parse_args()

    df = pd.read_csv(repo_root() / args.input, encoding="utf-8-sig")
    rank_col = "rank_density_corrected" if "rank_density_corrected" in df.columns else "composite_score_density_corrected"
    ascending = rank_col == "rank_density_corrected"
    ranked = df.sort_values(rank_col, ascending=ascending).head(args.top_n)
    columns = [
        "latitude",
        "longitude",
        "rho_mean",
        "annual_energy_density_corrected_mwh_mean",
        "capacity_factor_density_corrected_mean",
        "n_turbines_density_corrected",
        "installed_capacity_density_corrected_mw",
        "rank_density_corrected",
    ]
    columns = [col for col in columns if col in ranked.columns]
    print(ranked[columns].to_string(index=False))


if __name__ == "__main__":
    main()
