# Python Data Analytics & Time-Series Portfolio

A structured collection of exploratory data analysis (EDA), REST API ingestion pipelines, and time-series analytics implemented with Python and Pandas.

## Project Structure

```text
├── climate_analytics/          # Weather API ingestion & time-series analysis
│   ├── Projekt_Klimat.py       # Main pipeline script
│   └── poznan_climate_2025.png # Generated trend visualization
├── warehouse_eda/              # Inventory & supply chain data exploration
│   ├── Analiza_EDA.py          # Exploratory analysis script
│   └── magazyn_dane.csv        # Tabular warehouse dataset
├── .gitignore
└── README.md

1. Poznań Climate Analytics Pipeline (climate_analytics)

An automated data pipeline extracting and analyzing historical meteorological metrics for Poznań (2025).

    Data Ingestion: Fetches real-time historical weather records from the Open-Meteo Historical Archive REST API.

    Data Transformation: Resamples high-frequency daily observations into monthly aggregations using Pandas resample('ME').

    Visualization: Dual-layer Matplotlib charting comparing raw daily variances against smoothed seasonal trendlines.

    Engineering Decision: Migrated away from deprecated third-party wrappers to direct, resilient HTTP requests, ensuring forward compatibility with Pandas 3.x.

2. Warehouse Inventory EDA (warehouse_eda)

Exploratory Data Analysis examining stock levels, distributions, and inventory turnover patterns.

    Data Source: Tabular warehouse dataset (magazyn_dane.csv).

    Methods: Missing value handling, grouped aggregations (groupby), anomaly detection, and distribution analysis.

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

    pip install pandas requests matplotlib

  4. Run the scripts:
    Bash

    # Run Climate Pipeline
    python climate_analytics/Projekt_Klimat.py

    # Run Warehouse EDA
    python warehouse_eda/Analiza_EDA.py