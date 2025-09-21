# Data Directory

This directory contains geospatial data files for analysis.

## Structure
- `raw/vector/` - Original vector data (shapefiles, GeoJSON, etc.)
- `raw/raster/` - Original raster data (TIFF, imagery, etc.)  
- `processed/` - Cleaned and processed datasets
- `external/` - External datasets and downloads

## Important Notes
- **Data files are not tracked in Git** due to size limitations
- Place your data files in appropriate subdirectories
- Use the provided utilities in `src/data_processing/` to load data
- Check `.gitignore` for excluded file types

## Supported Formats
- **Vector**: .shp, .geojson, .gpkg, .kml
- **Raster**: .tif, .tiff, .nc, .hdf
- **Tables**: .csv, .xlsx (for attribute data)

## Sample Data Structure
```
data/
├── raw/
│   ├── vector/
│   │   ├── shapefiles/
│   │   │   ├── countries.shp
│   │   │   ├── cities.shp
│   │   │   └── roads.shp
│   │   ├── geojson/
│   │   │   ├── boundaries.geojson
│   │   │   └── points_of_interest.geojson
│   │   └── other_formats/
│   └── raster/
│       ├── tiff/
│       │   ├── elevation.tif
│       │   └── landcover.tif
│       └── imagery/
│           ├── satellite_image.tif
│           └── aerial_photo.jpg
├── processed/
└── external/
```
