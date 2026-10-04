# Python Data Analytics & Time-Series Portfolio

A structured collection of exploratory data analysis (EDA), REST API ingestion pipelines, and time-series analytics implemented with Python and Pandas.

## Project Structure

```text
├── climate_analytics/          # Weather API ingestion & time-series analysis
│   ├── Projekt_Klimat.py       # Main pipeline script
│   └── poznan_climate_2025.png # Generated trend visualization
├── warehouse_eda/              # IT hardware pricing & inventory exploration
│   ├── Analiza_EDA.py          # Data hygiene & EDA script
│   └── magazyn_dane.csv        # Hardware inventory dataset
├── .gitignore
└── README.md

1. Poznań Climate Analytics Pipeline (climate_analytics)

An automated data pipeline extracting and analyzing historical meteorological metrics for Poznań (2025).

    Data Ingestion: Fetches real-time historical weather records from the Open-Meteo Historical Archive REST API.

    Data Transformation: Resamples high-frequency daily observations into monthly aggregations using Pandas resample('ME').

    Visualization: Dual-layer Matplotlib charting comparing raw daily variances against smoothed seasonal trendlines.

    Engineering Decision: Migrated away from deprecated third-party wrappers to direct, resilient HTTP requests, ensuring forward compatibility with Pandas 3.x.

2. IT Hardware Inventory & Pricing EDA (warehouse_eda)

Exploratory Data Analysis and data hygiene pipeline evaluating IT hardware valuations and category distributions across device tiers (Business, Workstation, Office, Consumer).

    Data Cleaning & Imputation: Automated handling of missing telemetry via statistical mean imputation (fillna()) and dataset integrity verification (isnull(), duplicated()).

    Segmentation & Aggregation: Grouped pricing benchmarks by device category (groupby), vendor-specific string filtering (str.contains), and premium tier segmentation (> 5,000 PLN).

    Visual Analytics: Multi-view Matplotlib visualizations including model price benchmarks (bar chart) and average category budget distribution (pie chart).

Tech Stack

    Language: Python 3.11+
    Data Manipulation: Pandas, NumPy
    Networking: Requests
    Visualization: Matplotlib
    
Installation & Setup

 1. Clone the repository:
    Bash

    git clone https://github.com/wiktoria215/python-data-analytics.git
    cd python-data-analytics

  2. Create and activate a virtual environment:
    Bash

    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On Linux/macOS:
    source venv/bin/activate

  3. Install required packages:
    Bash

    pip install pandas numpy requests matplotlib

  4. Run the scripts:
   # Run Climate Pipeline
    python climate_analytics/Projekt_Klimat.py

   # Run Warehouse EDA
    python warehouse_eda/Analiza_EDA.py