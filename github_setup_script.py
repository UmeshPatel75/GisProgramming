"""
Automated GitHub Setup Script for GIS Programming Project
Run this script to create all necessary files for GitHub repository

Usage: python github_setup.py
"""

from pathlib import Path
import os

def create_gitignore(base_path):
    """Create .gitignore file for geospatial project"""
    
    gitignore_content = '''# Data files (usually too large for GitHub)
data/raw/
data/external/
*.tif
*.tiff
*.shp
*.shx
*.dbf
*.prj
*.cpg
*.qpj
*.geojson
*.json
*.gpkg
*.kml
*.kmz
*.nc
*.hdf
*.h5

# Large processed data
data/processed/*.shp
data/processed/*.geojson
data/processed/*.gpkg
data/processed/*.tif

# Output files
output/figures/*.png
output/figures/*.jpg
output/figures/*.pdf
output/figures/*.svg
output/tables/*.csv
output/tables/*.xlsx
output/processed_data/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
PIPFILE.lock

# Virtual environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Jupyter Notebook
.ipynb_checkpoints
*/.ipynb_checkpoints/*

# IPython
profile_default/
ipython_config.py

# VS Code
.vscode/
*.code-workspace

# PyCharm
.idea/

# Operating System
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Temporary files
*.tmp
*.temp
*.log

# Credentials and API keys
.env
config/secrets.py
*.key
*.pem

# Large model files
*.pkl
*.pickle
*.model
*.h5

# Documentation builds
docs/_build/
'''
    
    gitignore_path = base_path / ".gitignore"
    with open(gitignore_path, 'w', encoding='utf-8') as f:
        f.write(gitignore_content)
    
    print(f"✓ Created .gitignore: {gitignore_path}")

def create_updated_readme(base_path):
    """Create GitHub-ready README.md"""
    
    readme_content = '''# GIS Programming Project 🗺️

A comprehensive geospatial analysis project structure for learning and implementing GIS programming with Python.

## 🚀 Project Overview

This project provides a professional structure for geospatial data analysis using Python, focusing on:
- **Vector Data Analysis** (Shapefiles, GeoJSON, etc.)
- **Raster Data Processing** (TIFF, Imagery, etc.)  
- **Spatial Analytics** and **Visualization**
- **Organized Workflow** for reproducible geospatial research

## 📁 Project Structure

```
GisProgramming/
├── 📂 data/                    # Data storage (not tracked in Git)
│   ├── raw/                    # Original data files
│   │   ├── vector/            # Shapefiles, GeoJSON, etc.
│   │   └── raster/            # TIFF, imagery, etc.
│   ├── processed/             # Cleaned/processed data
│   └── external/              # External datasets
├── 📓 notebooks/              # Jupyter notebooks
│   ├── exploratory/           # Data exploration
│   ├── analysis/              # Main analysis notebooks
│   └── visualization/         # Visualization notebooks  
├── 📦 src/                    # Source code modules
│   ├── config.py             # Project configuration
│   ├── data_processing/       # Data utilities
│   ├── analysis/             # Analysis functions
│   └── visualization/        # Plotting utilities
├── 📊 output/                 # Results (sample outputs tracked)
│   ├── figures/              # Charts and maps
│   ├── tables/               # Analysis results
│   └── processed_data/       # Final datasets
├── 📚 docs/                   # Documentation
└── 🧪 tests/                  # Unit tests
```

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/GisProgramming.git
cd GisProgramming
```

### 2. Install Dependencies
```bash
# Create virtual environment (recommended)
python -m venv gis_env
source gis_env/bin/activate  # On Windows: gis_env\\Scripts\\activate

# Install required packages
pip install -r requirements.txt
```

### 3. Verify Installation
```bash
python -c "import geopandas; print('✅ GeoPandas installed successfully!')"
```

## 📊 Quick Start

### Load and Analyze Vector Data
```python
# Import project modules
import sys
sys.path.append('src')

from config import Config
from data_processing.vector_utils import VectorDataProcessor

# Initialize
config = Config()
processor = VectorDataProcessor()

# Load your data (place files in data/raw/vector/)
gdf = processor.load_vector_data("your_file.shp")

# Basic analysis
print(f"Loaded {len(gdf)} features")
print(f"CRS: {gdf.crs}")
```

### Run Analysis Notebooks
```bash
jupyter notebook notebooks/analysis/vector_data_analysis.ipynb
```

## 🔧 Core Dependencies

- **GeoPandas** - Vector data processing
- **Rasterio** - Raster data handling  
- **Shapely** - Geometric operations
- **Matplotlib/Seaborn** - Visualization
- **Pandas/NumPy** - Data analysis
- **Jupyter** - Interactive analysis

## 📖 Learning Path

1. **Start with**: `notebooks/analysis/vector_data_analysis.ipynb`
2. **Explore**: Basic geospatial operations and visualizations
3. **Advance to**: Spatial analysis and custom workflows
4. **Build**: Your own geospatial analysis projects

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-analysis`)
3. Commit your changes (`git commit -m 'Add amazing analysis'`)
4. Push to branch (`git push origin feature/amazing-analysis`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built for learning **Geospatial Analytics with Python**
- Structured for **Supply Chain** and **Marketing Analytics** integration
- Designed for **Power BI** and **Excel** workflow compatibility

---

**Happy Mapping!** 🗺️📊✨
'''
    
    readme_path = base_path / "README.md"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"✓ Updated README.md: {readme_path}")

def create_license(base_path):
    """Create MIT LICENSE file"""
    
    license_content = '''MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
    
    license_path = base_path / "LICENSE"
    with open(license_path, 'w', encoding='utf-8') as f:
        f.write(license_content)
    
    print(f"✓ Created LICENSE: {license_path}")

def create_data_readme(base_path):
    """Create README for data directory"""
    
    data_readme_content = '''# Data Directory

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
'''
    
    data_readme_path = base_path / "data" / "README.md"
    with open(data_readme_path, 'w', encoding='utf-8') as f:
        f.write(data_readme_content)
    
    print(f"✓ Created data/README.md: {data_readme_path}")

def create_output_readme(base_path):
    """Create README for output directory"""
    
    output_readme_content = '''# Output Directory

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
'''
    
    output_readme_path = base_path / "output" / "README.md"
    with open(output_readme_path, 'w', encoding='utf-8') as f:
        f.write(output_readme_content)
    
    print(f"✓ Created output/README.md: {output_readme_path}")

def create_github_actions(base_path):
    """Create GitHub Actions workflow"""
    
    # Create .github/workflows directory
    workflows_dir = base_path / ".github" / "workflows"
    workflows_dir.mkdir(parents=True, exist_ok=True)
    
    workflow_content = '''name: Test GIS Environment

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: '3.11'
    
    - name: Install GDAL
      run: |
        sudo apt-get update
        sudo apt-get install gdal-bin libgdal-dev
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Test imports
      run: |
        python -c "import geopandas; print('✅ GeoPandas works')"
        python -c "import rasterio; print('✅ Rasterio works')"
        python -c "import sys; sys.path.append('src'); from config import Config; print('✅ Config works')"
'''
    
    workflow_path = workflows_dir / "test.yml"
    with open(workflow_path, 'w', encoding='utf-8') as f:
        f.write(workflow_content)
    
    print(f"✓ Created GitHub Actions workflow: {workflow_path}")

def create_sample_output_files(base_path):
    """Create sample output files to demonstrate structure"""
    
    # Create a sample figure placeholder
    figures_dir = base_path / "output" / "figures"
    sample_figure_readme = figures_dir / "README.md"
    
    figure_readme_content = '''# Figures Directory

This directory contains visualizations and charts generated from geospatial analysis.

## Guidelines
- Use descriptive filenames
- Include date/version in filename if applicable  
- Save in appropriate format (PNG for web, PDF for print)
- Keep file sizes reasonable for Git tracking

## Sample Files
- `vector_analysis_demo.png` - Demonstration plot from notebook
- `spatial_analysis_results.png` - Results from spatial operations
'''
    
    with open(sample_figure_readme, 'w', encoding='utf-8') as f:
        f.write(figure_readme_content)
    
    print(f"✓ Created sample output structure")

def print_git_commands(base_path):
    """Print Git commands for user to run"""
    
    git_commands = f"""
🚀 GitHub Setup Complete! 

📂 Project location: {base_path}

🔧 Next Steps:

1. 📥 Initialize Git repository (in VS Code terminal):
   cd {base_path}
   git init
   git add .
   git commit -m "Initial commit: GIS Programming project structure"

2. 🌐 Create GitHub repository:
   - Go to https://github.com/new
   - Repository name: GisProgramming
   - Description: "Geospatial analysis project for learning GIS programming with Python"
   - Don't initialize with README (you already have one)
   - Click "Create Repository"

3. 🔗 Connect to GitHub:
   git remote add origin https://github.com/YOUR_USERNAME/GisProgramming.git
   git branch -M main
   git push -u origin main

4. ✅ Verify setup:
   Visit your GitHub repository to see your project!

📋 VS Code Git Workflow:
- Ctrl+Shift+G: Open Source Control
- Stage changes: Click "+" next to files
- Commit: Enter message and press Ctrl+Enter
- Push: Click sync button or use "git push"

🎯 Best Practices:
- ✅ Commit often with descriptive messages
- ✅ Never commit large data files (already in .gitignore)
- ✅ Use branches for major features
- ✅ Pull before pushing when collaborating
"""
    
    print(git_commands)

def main():
    """Main function to set up GitHub files"""
    
    base_path = Path(r"E:\GeoSpatial_Python\GisProgramming")
    
    print("🚀 Setting up GitHub files for GIS Programming project...")
    print("=" * 60)
    
    try:
        # Create all GitHub-related files
        create_gitignore(base_path)
        create_updated_readme(base_path)
        create_license(base_path)
        create_data_readme(base_path)
        create_output_readme(base_path)
        create_github_actions(base_path)
        create_sample_output_files(base_path)
        
        print("\n" + "=" * 60)
        print("✅ All GitHub setup files created successfully!")
        
        # Print next steps
        print_git_commands(base_path)
        
        return True
        
    except Exception as e:
        print(f"❌ Error setting up GitHub files: {e}")
        return False

if __name__ == "__main__":
    success = main()
    if success:
        print("\n🎉 Ready for GitHub! Follow the steps above to complete setup.")
    else:
        print("\n💥 Setup failed. Please check the error messages above.")
