# Data Notes

The `processed/` directory contains the CSV files used for the main tabulated and figure-level results.

- `hainan_candidate_points_with_constraints.csv`: candidate-level wind-resource indicators, proxy-constraint attributes, scores, and installed-capacity fields for Hainan Prefecture.
- `hainan_top10_candidates.csv`: the top 10 candidate nodes ranked by the baseline composite score.
- `reference_site_comparison.csv`: comparison between the operational reference site and the selected candidate under the 1.0 TWh/year electricity supply target.
- `density_corrected_results.csv`: candidate-level results after air-density correction, including corrected AEP, CF, FLH, turbine number, installed capacity, and ranking fields.
- `forecasting_metrics.csv`: forecasting error metrics for the reference and selected sites at the reported horizons.

## Abbreviations

AEP = annual energy production
CF = capacity factor
FLH = full-load hours
NWT = required turbine number
Dload = distance to load center
Dtown = distance to nearest resident town
nMAE = normalized mean absolute error
nRMSE = normalized root mean square error

## Coordinates and Units

Latitude and longitude are reported in decimal degrees.

AEP is reported in MWh per turbine. Installed capacity is reported in MW. Distances are reported in km where applicable.

## Raw ERA5 Data

Raw ERA5 hourly files are not included. They can be obtained from the Copernicus Climate Data Store using the variables and temporal coverage described in the manuscript.
