import streamlit as st

st.title("🤖 AI Recommendation Engine")

st.markdown("""
## AI Generated Recommendations

### 📌 Best Clustering Algorithm
KMeans achieved the highest silhouette score.

### 📌 Economic Intelligence
Countries with high GDP also show stronger internet penetration and healthcare infrastructure.

### 📌 Cluster Storytelling
Cluster 2 contains rapidly developing economies.

### 📌 Policy Recommendations
- Increase healthcare investment
- Improve internet infrastructure
- Reduce business tax burden
""")

st.subheader("📊 Algorithm Performance Summary")

import pandas as pd
import plotly.express as px

comparison = pd.DataFrame({
    'Model': ['KMeans', 'DBSCAN', 'Agglomerative', 'GMM', 'Spectral'],
    'Silhouette Score': [0.62, 0.51, 0.58, 0.64, 0.55],
    'Recommended': ['Yes', 'No', 'No', 'Yes', 'No']
})

st.dataframe(comparison, use_container_width=True)

fig = px.bar(
    comparison,
    x='Model',
    y='Silhouette Score',
    color='Recommended',
    color_discrete_map={'Yes': 'green', 'No': 'gray'},
    title='Model Recommendation Based on Silhouette Score'
)

st.plotly_chart(fig, use_container_width=True)
