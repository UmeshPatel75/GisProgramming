"""
Automated GIS Programming Project Setup Script
Run this script to create the complete project structure at E:\GeoSpatial_Python\GisProgramming

Author: Assistant
Date: Created for GIS Programming project setup
"""

import os
from pathlib import Path
import sys

def create_project_structure():
    """Create the complete GIS programming project structure"""
    
    # Base project path
    base_path = Path(r"E:\GeoSpatial_Python\GisProgramming")
    
    print(f"Creating GIS Programming project at: {base_path}")
    print("=" * 60)
    
    # Define the folder structure
    folders = [
        # Data folders
        "data/raw/vector/shapefiles",
        "data/raw/vector/geojson", 
        "data/raw/vector/other_formats",
        "data/raw/raster/tiff",
        "data/raw/raster/imagery",
        "data/raw/raster/other_formats",
        "data/processed",
        "data/external",
        
        # Notebooks folders
        "notebooks/exploratory",
        "notebooks/analysis", 
        "notebooks/visualization",
        
        # Source code folders
        "src/data_processing",
        "src/analysis",
        "src/visualization",
        
        # Output folders
        "output/figures",
        "output/tables",
        "output/processed_data",
        
        # Documentation and tests
        "docs",
        "tests"
    ]
    
    # Create all folders
    print("📁 Creating folder structure...")
    for folder in folders:
        folder_path = base_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"  ✓ {folder}")
    
    return base_path

def create_config_file(base_path):
    """Create the main configuration file"""
    
    config_content = '''"""
Project Configuration
Path: E:\\GeoSpatial_Python\\GisProgramming\\src\\config.py
"""

from pathlib import Path
import os

class Config:
    """Configuration class for GIS Programming project"""
    
    # Base project directory
    PROJECT_ROOT = Path(r"E:\\GeoSpatial_Python\\GisProgramming")
    
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
'''
    
    config_file = base_path / "src" / "config.py"
    with open(config_file, 'w') as f:
        f.write(config_content)
    
    print(f"  ✓ Configuration file created: {config_file}")

def create_vector_utils(base_path):
    """Create vector utilities file"""
    
    vector_utils_content = '''"""
Vector Data Processing Utilities
Path: E:\\GeoSpatial_Python\\GisProgramming\\src\\data_processing\\vector_utils.py
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
'''
    
    vector_utils_file = base_path / "src" / "data_processing" / "vector_utils.py"
    with open(vector_utils_file, 'w') as f:
        f.write(vector_utils_content)
    
    print(f"  ✓ Vector utilities created: {vector_utils_file}")

def create_init_files(base_path):
    """Create __init__.py files for Python packages"""
    
    init_files = [
        ("src/__init__.py", '"""GIS Programming Package"""\n__version__ = "1.0.0"'),
        ("src/data_processing/__init__.py", '"""Data Processing Module"""\nfrom .vector_utils import VectorDataProcessor, load_vector_data'),
        ("src/analysis/__init__.py", '"""Spatial Analysis Module"""'),
        ("src/visualization/__init__.py", '"""Visualization Module"""')
    ]
    
    for file_path, content in init_files:
        full_path = base_path / file_path
        with open(full_path, 'w') as f:
            f.write(content)
        print(f"  ✓ {file_path}")

def create_requirements_file(base_path):
    """Create requirements.txt file"""
    
    requirements_content = '''# Geospatial libraries
geopandas>=0.14.0
rasterio>=1.3.0
shapely>=2.0.0
fiona>=1.8.0
pyproj>=3.4.0

# Data analysis
pandas>=2.0.0
numpy>=1.24.0
scipy>=1.10.0

# Visualization
matplotlib>=3.7.0
seaborn>=0.12.0
folium>=0.14.0

# Jupyter and development
jupyter>=1.0.0
ipykernel>=6.0.0
notebook>=6.5.0

# Other utilities
pathlib2>=2.3.0
tqdm>=4.65.0
'''
    
    requirements_file = base_path / "requirements.txt"
    with open(requirements_file, 'w') as f:
        f.write(requirements_content)
    
    print(f"  ✓ Requirements file created: {requirements_file}")

def create_readme_file(base_path):
    """Create README.md file"""
    
    readme_content = '''# GIS Programming Project

## Project Structure
```
E:\\GeoSpatial_Python\\GisProgramming\\
```

## Setup Instructions

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Or create conda environment:
```bash
conda create -n gisprogramming python=3.11
conda activate gisprogramming
pip install -r requirements.txt
```

## Usage

1. Place your data files in appropriate directories:
   - Shapefiles: `data/raw/vector/shapefiles/`
   - GeoJSON: `data/raw/vector/geojson/`
   - Raster data: `data/raw/raster/`

2. Open Jupyter notebooks:
```bash
jupyter notebook notebooks/analysis/
```

## Directory Structure

- `data/`: All data files (raw, processed, external)
- `notebooks/`: Jupyter notebooks for analysis
- `src/`: Source code and utilities
- `output/`: Results and visualizations
- `docs/`: Documentation
- `tests/`: Test files

## Quick Start

```python
# Import the configuration and utilities
import sys
sys.path.append(r"E:\\GeoSpatial_Python\\GisProgramming\\src")

from config import Config
from data_processing.vector_utils import VectorDataProcessor

# Initialize
config = Config()
processor = VectorDataProcessor()

# Load your data
gdf = processor.load_vector_data("your_file.shp")
```
'''
    
    readme_file = base_path / "README.md"
    with open(readme_file, 'w') as f:
        f.write(readme_content)
    
    print(f"  ✓ README file created: {readme_file}")

def create_notebook_template(base_path):
    """Create a template notebook for vector analysis"""
    
    notebook_content = '''{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Vector Data Analysis\\n",
    "\\n",
    "**Project:** GIS Programming\\n",
    "**Path:** E:\\\\GeoSpatial_Python\\\\GisProgramming\\\\notebooks\\\\analysis\\\\vector_data_analysis.ipynb\\n",
    "**Purpose:** Analyze vector geospatial data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Setup and Configuration\\n",
    "import sys\\n",
    "from pathlib import Path\\n",
    "\\n",
    "# Add src directory to path\\n",
    "project_root = Path(r\\"E:\\\\GeoSpatial_Python\\\\GisProgramming\\")\\n",
    "src_path = project_root / \\"src\\"\\n",
    "sys.path.append(str(src_path))\\n",
    "\\n",
    "# Import necessary libraries\\n",
    "import geopandas as gpd\\n",
    "import pandas as pd\\n",
    "import matplotlib.pyplot as plt\\n",
    "import seaborn as sns\\n",
    "from config import Config\\n",
    "from data_processing.vector_utils import VectorDataProcessor\\n",
    "\\n",
    "# Initialize configuration and processors\\n",
    "config = Config()\\n",
    "vector_processor = VectorDataProcessor()\\n",
    "\\n",
    "print(\\"✅ Setup complete!\\")\\n",
    "print(f\\"Project root: {config.PROJECT_ROOT}\\")\\n",
    "print(f\\"Data directory: {config.DATA_DIR}\\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Check Available Data\\n",
    "available_files = vector_processor.list_available_files()\\n",
    "\\n",
    "print(\\"Available Vector Files:\\")\\n",
    "for file_type, files in available_files.items():\\n",
    "    print(f\\"\\\\n{file_type.upper()}:\\")\\n",
    "    for file in files:\\n",
    "        print(f\\"  - {file.name}\\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load Vector Data\\n",
    "# Replace 'your_file.shp' with your actual filename\\n",
    "try:\\n",
    "    # gdf = vector_processor.load_vector_data(\\"your_file.shp\\")\\n",
    "    \\n",
    "    # For demonstration, create sample data\\n",
    "    from shapely.geometry import Point\\n",
    "    sample_data = {\\n",
    "        'id': [1, 2, 3, 4, 5],\\n",
    "        'name': ['Point A', 'Point B', 'Point C', 'Point D', 'Point E'],\\n",
    "        'value': [10, 20, 15, 25, 30],\\n",
    "        'geometry': [Point(x, y) for x, y in [(1, 1), (2, 2), (3, 1), (4, 3), (5, 2)]]\\n",
    "    }\\n",
    "    gdf = gpd.GeoDataFrame(sample_data, crs='EPSG:4326')\\n",
    "    \\n",
    "    print(f\\"✅ Data loaded successfully!\\")\\n",
    "    print(f\\"Shape: {gdf.shape}\\")\\n",
    "    print(f\\"CRS: {gdf.crs}\\")\\n",
    "    print(\\"\\\\nFirst 5 rows:\\")\\n",
    "    display(gdf.head())\\n",
    "    \\n",
    "except Exception as e:\\n",
    "    print(f\\"❌ Error loading data: {e}\\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Data Visualization\\n",
    "fig, ax = plt.subplots(figsize=(10, 8))\\n",
    "gdf.plot(ax=ax, color='blue', markersize=100, alpha=0.7)\\n",
    "ax.set_title('Vector Data Visualization', fontsize=16, fontweight='bold')\\n",
    "ax.set_xlabel('X Coordinate')\\n",
    "ax.set_ylabel('Y Coordinate')\\n",
    "plt.grid(True, alpha=0.3)\\n",
    "plt.tight_layout()\\n",
    "\\n",
    "# Save figure\\n",
    "output_path = config.FIGURES_DIR / \\"vector_analysis_demo.png\\"\\n",
    "plt.savefig(output_path, dpi=300, bbox_inches='tight')\\n",
    "print(f\\"Figure saved to: {output_path}\\")\\n",
    "\\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}'''
    
    notebook_file = base_path / "notebooks" / "analysis" / "vector_data_analysis.ipynb"
    with open(notebook_file, 'w') as f:
        f.write(notebook_content)
    
    print(f"  ✓ Notebook template created: {notebook_file}")

def main():
    """Main function to create the complete project"""
    
    print("🚀 GIS Programming Project Setup")
    print("=" * 50)
    
    try:
        # Create folder structure
        base_path = create_project_structure()
        
        # Create essential files
        print("\\n📄 Creating essential files...")
        create_config_file(base_path)
        create_vector_utils(base_path)
        create_init_files(base_path)
        create_requirements_file(base_path)
        create_readme_file(base_path)
        create_notebook_template(base_path)
        
        print("\\n" + "=" * 50)
        print("✅ SUCCESS! Project created successfully!")
        print(f"📁 Project location: {base_path}")
        print("\\n📋 Next Steps:")
        print("1. Navigate to the project directory")
        print("2. Install dependencies: pip install -r requirements.txt")
        print("3. Place your data files in data/raw/vector/ or data/raw/raster/")
        print("4. Open Jupyter: jupyter notebook notebooks/analysis/vector_data_analysis.ipynb")
        print("5. Start analyzing your geospatial data!")
        
        return base_path
        
    except Exception as e:
        print(f"❌ Error creating project: {e}")
        return None

if __name__ == "__main__":
    project_path = main()
    if project_path:
        print(f"\\n🎉 Ready to start your geospatial analysis journey!")
    else:
        print("\\n💥 Setup failed. Please check the error messages above.")
