# Capacity-Efficient Wind-Power Planning for Plateau Energy Transition

This repository contains processed datasets, scripts, and figure files associated with the manuscript "Capacity-Efficient Wind-Power Planning for Plateau Energy Transition Using ERA5 Resource Assessment, Proxy Constraints, and Installed-Capacity Inversion".

## Data Sources

ERA5 hourly reanalysis data were downloaded from the Copernicus Climate Data Store by the authors. Raw ERA5 files are not redistributed here because of file size and reproducibility considerations.

## What Is Included

- processed candidate-level datasets
- candidate evaluation results
- installed-capacity inversion results
- air-density-corrected results
- forecasting metrics
- scripts used for analysis and figure/table generation
- supplementary table and figure

## What Is Not Included

- raw ERA5 hourly files
- large intermediate files
- journal submission files such as manuscript.docx and cover letter

## Repository Structure

- `data/processed/`: cleaned tables used for candidate ranking, comparison, air-density correction, and forecasting metrics.
- `src/`: Python scripts for checking or regenerating the main processed summaries from the included tables.
- `figures/`: manuscript figure files renamed by figure number and content.
- `supplementary/`: Supplementary Table S1 and Supplementary Figure S1.

## Reproducibility Note

Processed datasets are provided to reproduce the main tables and figure-level results. Raw ERA5 retrieval requires access to the Copernicus Climate Data Store. Processed datasets are provided for reproducing the tabulated and figure-level outputs, while raw ERA5 retrieval should be performed separately from the Copernicus Climate Data Store.

## Citation

If you use this repository, please cite the associated manuscript. A DOI-linked archived version will be added after release.

## License

Code is released under the MIT License. Processed datasets are provided for academic reproducibility. Users should also respect the original ERA5 data terms from the Copernicus Climate Data Store.
