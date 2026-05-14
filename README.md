# 🌍 Global Development AI Intelligence Platform

An advanced AI-powered Streamlit application for clustering analysis and economic intelligence.

## Features

- 🧠 Interactive Clustering Lab (KMeans, DBSCAN, Agglomerative, GMM, Spectral, Mean Shift)
- 📈 EDA Analytics Center
- 🗺️ Global Development Map
- 🌍 Country Intelligence Insights
- ⚡ Model Comparison Center
- 🤖 AI Recommendation Engine
- 📊 PCA Visualization

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

## Project Structure

```
Global_Development_AI_Platform/
├── app.py
├── requirements.txt
├── README.md
├── dataset/
│   └── world_development_measurement.xlsx   ← Add your dataset here
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_Dataset_Explorer.py
│   ├── 3_EDA_Analytics.py
│   ├── 4_Clustering_Lab.py
│   ├── 5_Model_Comparison.py
│   ├── 6_Global_Map.py
│   ├── 7_Country_Insights.py
│   └── 8_AI_Recommendations.py
├── utils/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── clustering.py
│   ├── visualizations.py
│   └── insights.py
├── css/
│   └── style.css
└── models/
```

## Dataset

Place your `world_development_measurement.xlsx` file inside the `dataset/` folder.
The dataset should contain a `Country` column and numeric development indicators.

## Deployment

Deploy easily on:
- Streamlit Cloud
- Render
- Railway
- HuggingFace Spaces
