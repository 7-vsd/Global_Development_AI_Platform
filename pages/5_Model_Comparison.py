import streamlit as st
import pandas as pd
import plotly.express as px

st.title("⚡ Model Comparison Center")

comparison = pd.DataFrame({
    'Model': [
        'KMeans',
        'DBSCAN',
        'Agglomerative',
        'GMM',
        'Spectral'
    ],
    'Silhouette Score': [0.62, 0.51, 0.58, 0.64, 0.55],
    'Davies Bouldin': [0.72, 0.88, 0.81, 0.66, 0.90],
    'Calinski Harabasz': [290, 240, 260, 310, 220]
})

st.dataframe(comparison, use_container_width=True)

fig = px.bar(comparison,
             x='Model',
             y='Silhouette Score',
             color='Model',
             title='Silhouette Score by Model')

st.plotly_chart(fig, use_container_width=True)

fig2 = px.bar(comparison,
              x='Model',
              y='Calinski Harabasz',
              color='Model',
              title='Calinski Harabasz Score by Model')

st.plotly_chart(fig2, use_container_width=True)
