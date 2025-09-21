"""
Create the notebook template manually (Windows compatible)
Save this as create_notebook.py and run it to complete your setup
"""

import json
from pathlib import Path

def create_notebook_template():
    """Create a clean notebook template without Unicode issues"""
    
    base_path = Path(r"E:\GeoSpatial_Python\GisProgramming")
    
    # Create the notebook content as a Python dictionary
    notebook_content = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# Vector Data Analysis\n",
                    "\n",
                    "**Project:** GIS Programming  \n",
                    "**Path:** E:\\GeoSpatial_Python\\GisProgramming\\notebooks\\analysis\\vector_data_analysis.ipynb  \n",
                    "**Purpose:** Analyze vector geospatial data\n",
                    "\n",
                    "## Setup Instructions\n",
                    "1. Place your vector data files in: `data/raw/vector/shapefiles/` or `data/raw/vector/geojson/`\n",
                    "2. Run the cells below to start your analysis\n",
                    "3. Modify the filename in the data loading section to match your actual data files"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Setup and Configuration\n",
                    "import sys\n",
                    "from pathlib import Path\n",
                    "\n",
                    "# Add src directory to path\n",
                    "project_root = Path(r\"E:\\GeoSpatial_Python\\GisProgramming\")\n",
                    "src_path = project_root / \"src\"\n",
                    "sys.path.append(str(src_path))\n",
                    "\n",
                    "# Import necessary libraries\n",
                    "import geopandas as gpd\n",
                    "import pandas as pd\n",
                    "import matplotlib.pyplot as plt\n",
                    "import seaborn as sns\n",
                    "from config import Config\n",
                    "from data_processing.vector_utils import VectorDataProcessor\n",
                    "\n",
                    "# Initialize configuration and processors\n",
                    "config = Config()\n",
                    "vector_processor = VectorDataProcessor()\n",
                    "\n",
                    "print(\"Setup complete!\")\n",
                    "print(f\"Project root: {config.PROJECT_ROOT}\")\n",
                    "print(f\"Data directory: {config.DATA_DIR}\")"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Check Available Data\n",
                    "available_files = vector_processor.list_available_files()\n",
                    "\n",
                    "print(\"Available Vector Files:\")\n",
                    "for file_type, files in available_files.items():\n",
                    "    print(f\"\\n{file_type.upper()}:\")\n",
                    "    if files:\n",
                    "        for file in files:\n",
                    "            print(f\"  - {file.name}\")\n",
                    "    else:\n",
                    "        print(\"  No files found\")\n",
                    "        \n",
                    "print(\"\\nDirectory paths:\")\n",
                    "print(f\"Shapefiles: {config.SHAPEFILES_DIR}\")\n",
                    "print(f\"GeoJSON: {config.GEOJSON_DIR}\")"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Load Vector Data\n",
                    "# Replace 'your_file.shp' with your actual filename\n",
                    "try:\n",
                    "    # Method 1: Load specific file (uncomment and modify)\n",
                    "    # gdf = vector_processor.load_shapefile(\"your_file.shp\")\n",
                    "    # gdf = vector_processor.load_geojson(\"your_file.geojson\")\n",
                    "    \n",
                    "    # Method 2: Auto-detect format (uncomment and modify)\n",
                    "    # gdf = vector_processor.load_vector_data(\"your_file.shp\")\n",
                    "    \n",
                    "    # For demonstration, create sample data\n",
                    "    from shapely.geometry import Point\n",
                    "    sample_data = {\n",
                    "        'id': [1, 2, 3, 4, 5],\n",
                    "        'name': ['Point A', 'Point B', 'Point C', 'Point D', 'Point E'],\n",
                    "        'value': [10, 20, 15, 25, 30],\n",
                    "        'category': ['Type1', 'Type2', 'Type1', 'Type3', 'Type2'],\n",
                    "        'geometry': [Point(x, y) for x, y in [(1, 1), (2, 2), (3, 1), (4, 3), (5, 2)]]\n",
                    "    }\n",
                    "    gdf = gpd.GeoDataFrame(sample_data, crs='EPSG:4326')\n",
                    "    \n",
                    "    print(\"Data loaded successfully!\")\n",
                    "    print(f\"Shape: {gdf.shape}\")\n",
                    "    print(f\"CRS: {gdf.crs}\")\n",
                    "    print(f\"Geometry types: {gdf.geometry.type.unique()}\")\n",
                    "    print(\"\\nFirst 5 rows:\")\n",
                    "    display(gdf.head())\n",
                    "    \n",
                    "except Exception as e:\n",
                    "    print(f\"Error loading data: {e}\")\n",
                    "    print(\"\\nTroubleshooting:\")\n",
                    "    print(\"1. Make sure your data file is in the correct directory\")\n",
                    "    print(\"2. Check the filename and path\")\n",
                    "    print(\"3. Verify the file format is supported\")"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Data Exploration\n",
                    "if 'gdf' in locals():\n",
                    "    print(\"Data Information:\")\n",
                    "    print(gdf.info())\n",
                    "    \n",
                    "    print(\"\\nData Description:\")\n",
                    "    if len(gdf.select_dtypes(include=['number']).columns) > 0:\n",
                    "        print(gdf.describe())\n",
                    "    \n",
                    "    print(\"\\nSpatial Extent (Bounds):\")\n",
                    "    bounds = gdf.total_bounds\n",
                    "    print(f\"Min X: {bounds[0]:.6f}\")\n",
                    "    print(f\"Min Y: {bounds[1]:.6f}\")\n",
                    "    print(f\"Max X: {bounds[2]:.6f}\")\n",
                    "    print(f\"Max Y: {bounds[3]:.6f}\")\n",
                    "    \n",
                    "    print(\"\\nColumn Information:\")\n",
                    "    for col in gdf.columns:\n",
                    "        if col != 'geometry':\n",
                    "            print(f\"{col}: {gdf[col].dtype}\")\n",
                    "else:\n",
                    "    print(\"No data loaded. Please load data first.\")"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Basic Visualization\n",
                    "if 'gdf' in locals():\n",
                    "    fig, axes = plt.subplots(1, 2, figsize=(15, 6))\n",
                    "    \n",
                    "    # Simple plot\n",
                    "    gdf.plot(ax=axes[0], color='blue', markersize=100, alpha=0.7)\n",
                    "    axes[0].set_title('Simple Vector Plot', fontsize=14, fontweight='bold')\n",
                    "    axes[0].set_xlabel('X Coordinate')\n",
                    "    axes[0].set_ylabel('Y Coordinate')\n",
                    "    axes[0].grid(True, alpha=0.3)\n",
                    "    \n",
                    "    # Categorical plot (if categorical column exists)\n",
                    "    if 'category' in gdf.columns:\n",
                    "        gdf.plot(column='category', ax=axes[1], legend=True, markersize=100)\n",
                    "        axes[1].set_title('Categorical Plot', fontsize=14, fontweight='bold')\n",
                    "    else:\n",
                    "        # Value-based plot (if numeric column exists)\n",
                    "        numeric_cols = gdf.select_dtypes(include=['number']).columns\n",
                    "        if len(numeric_cols) > 0:\n",
                    "            col_to_plot = [col for col in numeric_cols if col != 'id'][0] if 'id' in numeric_cols else numeric_cols[0]\n",
                    "            gdf.plot(column=col_to_plot, ax=axes[1], legend=True, cmap='viridis', markersize=100)\n",
                    "            axes[1].set_title(f'Value Plot ({col_to_plot})', fontsize=14, fontweight='bold')\n",
                    "        else:\n",
                    "            gdf.plot(ax=axes[1], color='red', markersize=100, alpha=0.7)\n",
                    "            axes[1].set_title('Alternative Plot', fontsize=14, fontweight='bold')\n",
                    "    \n",
                    "    axes[1].set_xlabel('X Coordinate')\n",
                    "    axes[1].set_ylabel('Y Coordinate')\n",
                    "    axes[1].grid(True, alpha=0.3)\n",
                    "    \n",
                    "    plt.tight_layout()\n",
                    "    \n",
                    "    # Save figure\n",
                    "    output_path = config.FIGURES_DIR / \"vector_analysis_demo.png\"\n",
                    "    plt.savefig(output_path, dpi=300, bbox_inches='tight')\n",
                    "    print(f\"Figure saved to: {output_path}\")\n",
                    "    \n",
                    "    plt.show()\n",
                    "else:\n",
                    "    print(\"No data to visualize. Please load data first.\")"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Basic Spatial Analysis\n",
                    "if 'gdf' in locals():\n",
                    "    print(\"Performing basic spatial analysis...\")\n",
                    "    \n",
                    "    # Create buffer around geometries\n",
                    "    buffer_distance = 0.5  # Adjust based on your data's coordinate system\n",
                    "    gdf_buffered = gdf.copy()\n",
                    "    gdf_buffered['geometry'] = gdf.geometry.buffer(buffer_distance)\n",
                    "    \n",
                    "    print(f\"Created buffers with distance: {buffer_distance}\")\n",
                    "    \n",
                    "    # Calculate centroids (for polygons)\n",
                    "    gdf_centroids = gdf.copy()\n",
                    "    gdf_centroids['geometry'] = gdf.geometry.centroid\n",
                    "    \n",
                    "    # If polygons, calculate area\n",
                    "    if gdf.geometry.iloc[0].geom_type in ['Polygon', 'MultiPolygon']:\n",
                    "        gdf['area'] = gdf.geometry.area\n",
                    "        print(f\"Calculated areas. Mean area: {gdf['area'].mean():.6f}\")\n",
                    "    \n",
                    "    # Visualize analysis results\n",
                    "    fig, ax = plt.subplots(figsize=(12, 8))\n",
                    "    \n",
                    "    # Plot buffers\n",
                    "    gdf_buffered.plot(ax=ax, color='lightblue', alpha=0.5, label='Buffers')\n",
                    "    \n",
                    "    # Plot original data\n",
                    "    gdf.plot(ax=ax, color='darkblue', markersize=100, label='Original')\n",
                    "    \n",
                    "    # Plot centroids\n",
                    "    gdf_centroids.plot(ax=ax, color='red', markersize=50, label='Centroids')\n",
                    "    \n",
                    "    ax.set_title('Spatial Analysis Results', fontsize=16, fontweight='bold')\n",
                    "    ax.set_xlabel('X Coordinate')\n",
                    "    ax.set_ylabel('Y Coordinate')\n",
                    "    ax.legend()\n",
                    "    ax.grid(True, alpha=0.3)\n",
                    "    \n",
                    "    plt.tight_layout()\n",
                    "    \n",
                    "    # Save analysis figure\n",
                    "    analysis_output = config.FIGURES_DIR / \"spatial_analysis_results.png\"\n",
                    "    plt.savefig(analysis_output, dpi=300, bbox_inches='tight')\n",
                    "    print(f\"Analysis figure saved to: {analysis_output}\")\n",
                    "    \n",
                    "    plt.show()\n",
                    "    \n",
                    "    # Save processed data\n",
                    "    buffered_output = vector_processor.save_processed_data(\n",
                    "        gdf_buffered, \"demo_buffered_analysis\", format=\"shapefile\"\n",
                    "    )\n",
                    "    \n",
                    "    print(\"Spatial analysis completed successfully!\")\n",
                    "else:\n",
                    "    print(\"No data available for analysis. Please load data first.\")"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Next Steps\n",
                    "\n",
                    "### To work with your own data:\n",
                    "1. **Place your data files** in the appropriate directories:\n",
                    "   - Shapefiles: `data/raw/vector/shapefiles/`\n",
                    "   - GeoJSON files: `data/raw/vector/geojson/`\n",
                    "   - Other formats: `data/raw/vector/other_formats/`\n",
                    "\n",
                    "2. **Modify the data loading cell** above to use your actual filename\n",
                    "\n",
                    "3. **Customize the analysis** based on your data characteristics\n",
                    "\n",
                    "### Learn more about geospatial analysis:\n",
                    "- **Coordinate Reference Systems (CRS)**: Understanding projections\n",
                    "- **Spatial joins**: Combining datasets based on location\n",
                    "- **Geometric operations**: Buffers, intersections, unions\n",
                    "- **Spatial statistics**: Density, clustering, autocorrelation\n",
                    "- **Web mapping**: Interactive visualizations with Folium\n",
                    "\n",
                    "### Project structure recap:\n",
                    "```\n",
                    "E:\\GeoSpatial_Python\\GisProgramming\\\n",
                    "├── data/               # All your data files\n",
                    "├── notebooks/          # Analysis notebooks (you are here!)\n",
                    "├── src/               # Reusable code and utilities\n",
                    "├── output/            # Results and visualizations\n",
                    "└── docs/              # Documentation\n",
                    "```"
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
    }
    
    # Save the notebook
    notebook_file = base_path / "notebooks" / "analysis" / "vector_data_analysis.ipynb"
    
    with open(notebook_file, 'w', encoding='utf-8') as f:
        json.dump(notebook_content, f, indent=2, ensure_ascii=False)
    
    print(f"Notebook created successfully: {notebook_file}")
    return notebook_file

if __name__ == "__main__":
    try:
        notebook_path = create_notebook_template()
        print("\\nSetup completed successfully!")
        print("\\nNext steps:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Start Jupyter: jupyter notebook")
        print(f"3. Open: {notebook_path}")
    except Exception as e:
        print(f"Error: {e}")
