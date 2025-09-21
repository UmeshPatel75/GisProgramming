"""
Vector Data Processing Utilities
Path: E:\GeoSpatial_Python\GisProgramming\src\data_processing\vector_utils.py
"""

import geopandas as gpd
import pandas as pd
from pathlib import Path
from typing import Union, List, Optional
import warnings
import sys

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))
from config import Config

class VectorDataProcessor:
    """Class for processing vector geospatial data"""
    
    def __init__(self):
        self.config = Config()
    
    def load_shapefile(self, filename: str, subfolder: str = None) -> gpd.GeoDataFrame:
        """Load shapefile from shapefiles directory"""
        if subfolder:
            file_path = self.config.SHAPEFILES_DIR / subfolder / filename
        else:
            file_path = self.config.SHAPEFILES_DIR / filename
            
        if not file_path.exists():
            raise FileNotFoundError(f"Shapefile not found: {file_path}")
        
        return gpd.read_file(file_path)
    
    def load_geojson(self, filename: str, subfolder: str = None) -> gpd.GeoDataFrame:
        """Load GeoJSON from geojson directory"""
        if subfolder:
            file_path = self.config.GEOJSON_DIR / subfolder / filename
        else:
            file_path = self.config.GEOJSON_DIR / filename
            
        if not file_path.exists():
            raise FileNotFoundError(f"GeoJSON not found: {file_path}")
        
        return gpd.read_file(file_path)
    
    def load_vector_data(self, filename: str, data_format: str = "auto") -> gpd.GeoDataFrame:
        """Load vector data with automatic format detection"""
        file_path = None
        
        if data_format == "auto":
            # Try to find file in different directories
            possible_paths = [
                self.config.SHAPEFILES_DIR / filename,
                self.config.GEOJSON_DIR / filename,
                self.config.VECTOR_OTHER_DIR / filename,
                self.config.VECTOR_DIR / filename
            ]
            
            for path in possible_paths:
                if path.exists():
                    file_path = path
                    break
        else:
            file_path = self.config.get_data_path("vector", data_format) / filename
        
        if file_path is None or not file_path.exists():
            raise FileNotFoundError(f"Vector file not found: {filename}")
        
        return gpd.read_file(file_path)
    
    def save_processed_data(self, gdf: gpd.GeoDataFrame, filename: str, 
                           format: str = "shapefile") -> Path:
        """Save processed vector data"""
        if format.lower() in ["shapefile", "shp"]:
            output_path = self.config.PROCESSED_DATA_DIR / f"{filename}.shp"
        elif format.lower() in ["geojson", "json"]:
            output_path = self.config.PROCESSED_DATA_DIR / f"{filename}.geojson"
        else:
            output_path = self.config.PROCESSED_DATA_DIR / filename
        
        gdf.to_file(output_path)
        print(f"Data saved to: {output_path}")
        return output_path
    
    def list_available_files(self) -> dict:
        """List all available vector files"""
        files = {
            "shapefiles": list(self.config.SHAPEFILES_DIR.glob("*.shp")),
            "geojson": list(self.config.GEOJSON_DIR.glob("*.geojson")) + 
                      list(self.config.GEOJSON_DIR.glob("*.json")),
            "other": list(self.config.VECTOR_OTHER_DIR.glob("*"))
        }
        return files

def load_vector_data(filename: str, data_format: str = "auto") -> gpd.GeoDataFrame:
    """Convenience function to load vector data"""
    processor = VectorDataProcessor()
    return processor.load_vector_data(filename, data_format)
