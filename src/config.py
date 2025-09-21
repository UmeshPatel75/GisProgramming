"""
Project Configuration
Path: E:\GeoSpatial_Python\GisProgramming\src\config.py
"""

from pathlib import Path
import os

class Config:
    """Configuration class for GIS Programming project"""
    
    # Base project directory
    PROJECT_ROOT = Path(r"E:\GeoSpatial_Python\GisProgramming")
    
    # Data directories
    DATA_DIR = PROJECT_ROOT / "data"
    RAW_DATA_DIR = DATA_DIR / "raw"
    PROCESSED_DATA_DIR = DATA_DIR / "processed"
    EXTERNAL_DATA_DIR = DATA_DIR / "external"
    
    # Vector data directories
    VECTOR_DIR = RAW_DATA_DIR / "vector"
    SHAPEFILES_DIR = VECTOR_DIR / "shapefiles"
    GEOJSON_DIR = VECTOR_DIR / "geojson"
    VECTOR_OTHER_DIR = VECTOR_DIR / "other_formats"
    
    # Raster data directories
    RASTER_DIR = RAW_DATA_DIR / "raster"
    TIFF_DIR = RASTER_DIR / "tiff"
    IMAGERY_DIR = RASTER_DIR / "imagery"
    RASTER_OTHER_DIR = RASTER_DIR / "other_formats"
    
    # Notebooks directories
    NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
    EXPLORATORY_DIR = NOTEBOOKS_DIR / "exploratory"
    ANALYSIS_DIR = NOTEBOOKS_DIR / "analysis"
    VISUALIZATION_DIR = NOTEBOOKS_DIR / "visualization"
    
    # Source code directories
    SRC_DIR = PROJECT_ROOT / "src"
    DATA_PROCESSING_DIR = SRC_DIR / "data_processing"
    ANALYSIS_CODE_DIR = SRC_DIR / "analysis"
    VISUALIZATION_CODE_DIR = SRC_DIR / "visualization"
    
    # Output directories
    OUTPUT_DIR = PROJECT_ROOT / "output"
    FIGURES_DIR = OUTPUT_DIR / "figures"
    TABLES_DIR = OUTPUT_DIR / "tables"
    PROCESSED_OUTPUT_DIR = OUTPUT_DIR / "processed_data"
    
    # Other directories
    DOCS_DIR = PROJECT_ROOT / "docs"
    TESTS_DIR = PROJECT_ROOT / "tests"
    
    @classmethod
    def ensure_directories(cls):
        """Create all directories if they don't exist"""
        directories = [
            cls.DATA_DIR, cls.RAW_DATA_DIR, cls.PROCESSED_DATA_DIR, cls.EXTERNAL_DATA_DIR,
            cls.VECTOR_DIR, cls.SHAPEFILES_DIR, cls.GEOJSON_DIR, cls.VECTOR_OTHER_DIR,
            cls.RASTER_DIR, cls.TIFF_DIR, cls.IMAGERY_DIR, cls.RASTER_OTHER_DIR,
            cls.NOTEBOOKS_DIR, cls.EXPLORATORY_DIR, cls.ANALYSIS_DIR, cls.VISUALIZATION_DIR,
            cls.SRC_DIR, cls.DATA_PROCESSING_DIR, cls.ANALYSIS_CODE_DIR, cls.VISUALIZATION_CODE_DIR,
            cls.OUTPUT_DIR, cls.FIGURES_DIR, cls.TABLES_DIR, cls.PROCESSED_OUTPUT_DIR,
            cls.DOCS_DIR, cls.TESTS_DIR
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
    
    @classmethod
    def get_data_path(cls, data_type, file_format=None):
        """Get appropriate data path based on type and format"""
        if data_type == "vector":
            if file_format == "shapefile":
                return cls.SHAPEFILES_DIR
            elif file_format == "geojson":
                return cls.GEOJSON_DIR
            else:
                return cls.VECTOR_OTHER_DIR
        elif data_type == "raster":
            if file_format == "tiff":
                return cls.TIFF_DIR
            elif file_format == "imagery":
                return cls.IMAGERY_DIR
            else:
                return cls.RASTER_OTHER_DIR
        else:
            return cls.RAW_DATA_DIR
