"""Installed-capacity inversion for selected and reference sites."""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

E_TARGET_MWH = 1_000_000.0
ETA = 0.90
P_R_MW = 2.0


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def relative_change(selected, reference):
    if isinstance(reference, (int, float, np.integer, np.floating)) and not pd.isna(reference) and abs(float(reference)) > 1e-12:
        return (float(selected) - float(reference)) / float(reference)
    return np.nan


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/processed/hainan_candidate_points_with_constraints.csv")
    parser.add_argument("--output", default="data/processed/reference_site_comparison.csv")
    args = parser.parse_args()

    root = repo_root()
    df = pd.read_csv(root / args.input, encoding="utf-8-sig")
    df["n_turbines_recomputed"] = np.ceil(E_TARGET_MWH / (ETA * df["annual_energy_mwh_mean"])).astype(int)
    df["installed_capacity_recomputed_mw"] = df["n_turbines_recomputed"] * P_R_MW

    selected = df.sort_values("composite_score_v4", ascending=False).iloc[0]
    reference = df.loc[df["distance_to_reference_point"].idxmin()]
    indicators = [
        "latitude",
        "longitude",
        "annual_energy_mwh_mean",
        "capacity_factor_mean",
        "full_load_hours_mean",
        "low_ratio_mean",
        "distance_to_load_km",
        "nearest_town_name",
        "distance_to_nearest_town_km",
        "elevation_m",
        "slope_deg",
        "n_turbines_recomputed",
        "installed_capacity_recomputed_mw",
        "composite_score_v4",
    ]
    rows = []
    for col in indicators:
        rows.append({
            "indicator": col,
            "reference_site": reference[col],
            "selected_candidate": selected[col],
            "relative_change": relative_change(selected[col], reference[col]),
        })
    out = pd.DataFrame(rows)
    out.to_csv(root / args.output, index=False, encoding="utf-8-sig")
    print(out.to_string(index=False))


if __name__ == "__main__":
    main()
