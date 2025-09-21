# Output Directory

This directory contains analysis results and visualizations.

## Structure
- `figures/` - Charts, maps, and visualizations
- `tables/` - Analysis results and statistics  
- `processed_data/` - Final processed datasets

## File Organization
- Use descriptive filenames with dates/versions
- Group related outputs in subdirectories
- Include metadata files for complex analyses

## Sample Structure
```
output/
├── figures/
│   ├── exploratory/
│   │   ├── data_overview_2025-01-20.png
│   │   └── correlation_matrix.png
│   ├── analysis/
│   │   ├── spatial_distribution_map.png
│   │   ├── buffer_analysis_results.png
│   │   └── clustering_results.png
│   └── final/
│       ├── publication_ready_map.png
│       └── summary_dashboard.png
├── tables/
│   ├── summary_statistics.csv
│   ├── spatial_analysis_results.xlsx
│   └── model_performance_metrics.csv
└── processed_data/
    ├── cleaned_boundaries.geojson
    ├── aggregated_statistics.csv
    └── final_analysis_dataset.gpkg
```

## Note
- Sample outputs are tracked in Git for demonstration
- Large files are excluded via `.gitignore`
- Consider using Git LFS for important result files
