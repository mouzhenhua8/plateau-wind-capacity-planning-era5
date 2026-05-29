# CHECK_REPORT

Generated: 2026-05-29 17:24:47 Asia/Shanghai

## 1. Repository File Tree

```text
plateau-wind-capacity-planning-era5/
.gitignore
CHECK_REPORT.md
CITATION.cff
LICENSE
README.md
data/
    README.md
    processed/
        density_corrected_results.csv
        forecasting_metrics.csv
        hainan_candidate_points_with_constraints.csv
        hainan_top10_candidates.csv
        reference_site_comparison.csv
figures/
    Figure_1_framework.png
    Figure_2_resource_background.png
    Figure_3_top20_background.png
    Figure_4_proxy_constraints.png
    Figure_5_candidate_ranking.png
    Figure_6_planning_comparison.png
    Figure_7_density_correction.png
    Figure_8_weight_perturbation.png
requirements.txt
src/
    01_candidate_scoring.py
    02_installed_capacity_inversion.py
    03_air_density_correction.py
    04_weight_perturbation.py
    05_forecasting_diagnostics.py
supplementary/
    Supplementary_Figure_S1.png
    Supplementary_Table_S1.csv
unclassified/
    original_figure_6_unmapped.png
```

## 2. Source Classification

| Target | Source | Reason |
| --- | --- | --- |
| data/processed/hainan_candidate_points_with_constraints.csv | supplementary/data/processed/hainan_candidate_points_with_constraints_v4.csv | candidate points, proxy constraints, scores, and installed-capacity fields |
| data/processed/hainan_top10_candidates.csv | supplementary/data/processed/hainan_top10_candidates_with_constraints_v4.csv | top 10 selected candidates |
| data/processed/reference_site_comparison.csv | supplementary/data/processed/hainan_candidate_points_with_constraints_v4.csv plus hainan_reference_vs_best_comparison_with_constraints_v4.csv | reference versus selected-site comparison, exported with English column names |
| data/processed/density_corrected_results.csv | supplementary/data/processed/air_density_corrected_all_candidates_v4.csv | full-candidate density-corrected results |
| data/processed/forecasting_metrics.csv | supplementary/data/forecasting/forecasting_metrics_summary.csv | forecasting MAE/RMSE/nMAE/nRMSE metrics |
| figures/Figure_1_framework.png | figure.zip/10.png | Figure 1 framework |
| figures/Figure_2_resource_background.png | figure.zip/2.png | Figure 2 resource background |
| figures/Figure_3_top20_background.png | figure.zip/3.png | Figure 3 top-20 background |
| figures/Figure_4_proxy_constraints.png | figure.zip/4.png | Figure 4 proxy constraints |
| figures/Figure_5_candidate_ranking.png | figure.zip/8.png | Figure 5 candidate ranking |
| figures/Figure_6_planning_comparison.png | figure.zip/7.png | Figure 6 planning comparison |
| figures/Figure_7_density_correction.png | figure.zip/1.png | Figure 7 density correction |
| figures/Figure_8_weight_perturbation.png | figure.zip/9.png | Figure 8 weight perturbation |
| supplementary/Supplementary_Table_S1.csv | supplementary/data/processed/qinghai_top20_grid_cells.csv | Supplementary Table S1 |
| supplementary/Supplementary_Figure_S1.png | figure.zip/5.png | Supplementary Figure S1 forecasting diagnostics |
| unclassified/original_figure_6_unmapped.png | figure.zip/6.png | no current manuscript caption matched this original figure |

## 3. CSV Check Results

| File | Rows | Columns | Status | Notes |
| --- | ---: | ---: | --- | --- |
| data/processed/density_corrected_results.csv | 182 | 75 | ok | readable by pandas; no duplicate or all-empty columns detected |
| data/processed/forecasting_metrics.csv | 12 | 8 | ok | readable by pandas; no duplicate or all-empty columns detected |
| data/processed/hainan_candidate_points_with_constraints.csv | 182 | 42 | ok | readable by pandas; no duplicate or all-empty columns detected |
| data/processed/hainan_top10_candidates.csv | 10 | 42 | ok | readable by pandas; no duplicate or all-empty columns detected |
| data/processed/reference_site_comparison.csv | 14 | 4 | ok | readable by pandas; no duplicate or all-empty columns detected |
| supplementary/Supplementary_Table_S1.csv | 20 | 9 | ok | readable by pandas; no duplicate or all-empty columns detected |

### CSV Column Names

- `data/processed/density_corrected_results.csv`: latitude, longitude, avg_ws100_mean, avg_ws100_std, max_ws100_mean, min_ws100_mean, annual_energy_mwh_mean, annual_energy_mwh_std, annual_energy_gwh_mean, capacity_factor_mean, capacity_factor_std, full_load_hours_mean, full_load_hours_std, low_ratio_mean, high_ratio_mean, safe_ratio_mean, rated_ratio_mean, avg_ws100_cv, annual_energy_mwh_cv, capacity_factor_cv, distance_to_load_km, n_turbines, installed_capacity_mw, score_energy, score_cf, score_turbines, score_distance, score_lowrisk, composite_score, distance_to_control_point, elevation_m, slope_deg, nearest_town_name, distance_to_nearest_town_km, elevation_penalty, slope_penalty, score_town_dist, score_load_dist, score_elevation, score_slope, composite_score_v4, distance_to_reference_point, candidate_id, n_years, rho_mean, rho_std_mean, rho_interannual_std, ws100_raw_mean, ws100_density_eq_mean, annual_energy_raw_mwh_mean, annual_energy_raw_mwh_std, annual_energy_density_corrected_mwh_mean, annual_energy_density_corrected_mwh_std, capacity_factor_raw_mean, capacity_factor_density_corrected_mean, full_load_hours_raw_mean, full_load_hours_density_corrected_mean, low_ratio_raw_mean, low_ratio_density_corrected_mean, density_AEP_change_percent, raw_AEP_cv, density_corrected_AEP_cv, n_turbines_raw_recomputed, installed_capacity_raw_recomputed_mw, n_turbines_density_corrected, installed_capacity_density_corrected_mw, score_energy_density, score_cf_density, score_turbines_density, score_lowrisk_density, composite_score_density_corrected, rank_density_corrected, rank_original_v4, ranking_shift_density_minus_original, distance_to_reference_point_km
- `data/processed/forecasting_metrics.csv`: site_type, horizon, model, mae_kw, rmse_kw, nmae_percent, nrmse_percent, mape_above_50kw_percent
- `data/processed/hainan_candidate_points_with_constraints.csv`: latitude, longitude, avg_ws100_mean, avg_ws100_std, max_ws100_mean, min_ws100_mean, annual_energy_mwh_mean, annual_energy_mwh_std, annual_energy_gwh_mean, capacity_factor_mean, capacity_factor_std, full_load_hours_mean, full_load_hours_std, low_ratio_mean, high_ratio_mean, safe_ratio_mean, rated_ratio_mean, avg_ws100_cv, annual_energy_mwh_cv, capacity_factor_cv, distance_to_load_km, n_turbines, installed_capacity_mw, score_energy, score_cf, score_turbines, score_distance, score_lowrisk, composite_score, distance_to_control_point, elevation_m, slope_deg, nearest_town_name, distance_to_nearest_town_km, elevation_penalty, slope_penalty, score_town_dist, score_load_dist, score_elevation, score_slope, composite_score_v4, distance_to_reference_point
- `data/processed/hainan_top10_candidates.csv`: latitude, longitude, avg_ws100_mean, avg_ws100_std, max_ws100_mean, min_ws100_mean, annual_energy_mwh_mean, annual_energy_mwh_std, annual_energy_gwh_mean, capacity_factor_mean, capacity_factor_std, full_load_hours_mean, full_load_hours_std, low_ratio_mean, high_ratio_mean, safe_ratio_mean, rated_ratio_mean, avg_ws100_cv, annual_energy_mwh_cv, capacity_factor_cv, distance_to_load_km, n_turbines, installed_capacity_mw, score_energy, score_cf, score_turbines, score_distance, score_lowrisk, composite_score, distance_to_control_point, elevation_m, slope_deg, nearest_town_name, distance_to_nearest_town_km, elevation_penalty, slope_penalty, score_town_dist, score_load_dist, score_elevation, score_slope, composite_score_v4, distance_to_reference_point
- `data/processed/reference_site_comparison.csv`: indicator, reference_site, selected_candidate, relative_change
- `supplementary/Supplementary_Table_S1.csv`: rank, latitude, longitude, ws100_mean, annual_energy_mwh_mean, capacity_factor_mean, full_load_hours_mean, wind_cv, aep_cv

## 4. Image Check Results

| File | Dimensions | Size | Status | Notes |
| --- | --- | ---: | --- | --- |
| figures/Figure_1_framework.png | 1589 x 892 | 371.2 KB | ok | opens successfully; filename matches expected target |
| figures/Figure_2_resource_background.png | 4150 x 3252 | 660.3 KB | ok | opens successfully; filename matches expected target |
| figures/Figure_3_top20_background.png | 4253 x 1935 | 957.2 KB | ok | opens successfully; filename matches expected target |
| figures/Figure_4_proxy_constraints.png | 3616 x 2389 | 851.7 KB | ok | opens successfully; filename matches expected target |
| figures/Figure_5_candidate_ranking.png | 7980 x 3699 | 1113.6 KB | ok | opens successfully; filename matches expected target |
| figures/Figure_6_planning_comparison.png | 10041 x 4438 | 900.2 KB | ok | opens successfully; filename matches expected target |
| figures/Figure_7_density_correction.png | 7011 x 2933 | 396.1 KB | ok | opens successfully; filename matches expected target |
| figures/Figure_8_weight_perturbation.png | 8841 x 3504 | 705.6 KB | ok | opens successfully; filename matches expected target |
| supplementary/Supplementary_Figure_S1.png | 7949 x 9763 | 1832.2 KB | ok | opens successfully; filename matches expected target |

## 5. Python Script Syntax Check

| File | py_compile | Notes |
| --- | --- | --- |
| src/01_candidate_scoring.py | ok | compiled with python -m py_compile |
| src/02_installed_capacity_inversion.py | ok | compiled with python -m py_compile |
| src/03_air_density_correction.py | ok | compiled with python -m py_compile |
| src/04_weight_perturbation.py | ok | compiled with python -m py_compile |
| src/05_forecasting_diagnostics.py | ok | compiled with python -m py_compile |

Absolute-path scan: No local absolute paths detected in src scripts.

Raw ERA5 note: `03_air_density_correction.py` summarizes the processed density-corrected table included here. Raw ERA5 hourly files are not included and should be retrieved separately from the Copernicus Climate Data Store if a full hourly recomputation is needed.

## 6. requirements.txt Basis

Generated by AST import scanning of files in `src/`.

- `src/01_candidate_scoring.py` imports: __future__, argparse, pandas, pathlib
- `src/02_installed_capacity_inversion.py` imports: __future__, argparse, numpy, pandas, pathlib
- `src/03_air_density_correction.py` imports: __future__, argparse, pandas, pathlib
- `src/04_weight_perturbation.py` imports: __future__, argparse, pandas, pathlib
- `src/05_forecasting_diagnostics.py` imports: __future__, argparse, pandas, pathlib

Final `requirements.txt` packages: numpy, pandas

## 7. Missing Files

None. All requested target files were created.

## 8. Unclassified Files

- `unclassified/original_figure_6_unmapped.png`: original `6.png` shows a candidate/reference-site location map, but the current manuscript captions map Figure 6 to the planning comparison panels from original `7.png`.

Detected source files not copied because they were outside the requested final structure or were intermediate/prediction tables: prediction CSVs, sensitivity scenario CSVs, input town/base CSVs, reference-scheme-only CSVs, and old source README/requirements files.

## 9. Large File Check

No files larger than 50 MB were found in the submit scan or final repository.

Raw ERA5-like extensions in final repository: None.

## 10. GitHub-ready Zip

Successfully generated `plateau-wind-capacity-planning-era5_GitHub_ready.zip` (7.21 MB). The archive contains the `plateau-wind-capacity-planning-era5/` folder only.

## 11. Suggested GitHub Upload Steps

1. Review `CHECK_REPORT.md`, `README.md`, and the files under `data/processed/`.
2. Create a new empty GitHub repository.
3. From the `plateau-wind-capacity-planning-era5/` directory, run `git init`, `git add .`, and `git commit -m "Initial data and code release"`.
4. Add the GitHub remote and push the main branch.
5. After archival release, update `CITATION.cff` and the README with the final DOI.
