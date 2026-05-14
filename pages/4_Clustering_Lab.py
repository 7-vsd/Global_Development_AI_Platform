import streamlit as st
import plotly.express as px
from sklearn.decomposition import PCA
from utils.data_loader import load_data
from utils.preprocessing import preprocess_data
from utils.clustering import (
    run_kmeans, run_dbscan, run_agglomerative,
    run_gmm, run_spectral, run_meanshift
)

st.title("🧠 Interactive Clustering Laboratory")

file_path = "dataset/world_development_measurement.xlsx"
df = load_data(file_path)

scaled, cols = preprocess_data(df)

algo = st.selectbox(
    "Select Algorithm",
    [
        "KMeans",
        "DBSCAN",
        "Agglomerative",
        "Gaussian Mixture",
        "Spectral",
        "Mean Shift"
    ]
)

n_clusters = st.slider("Clusters", 2, 10, 4)

if algo == "KMeans":
    labels = run_kmeans(scaled, n_clusters)

elif algo == "DBSCAN":
    eps = st.slider("EPS", 0.1, 5.0, 0.5)
    min_samples = st.slider("Min Samples", 2, 20, 5)
    labels = run_dbscan(scaled, eps, min_samples)

elif algo == "Agglomerative":
    labels = run_agglomerative(scaled, n_clusters)

elif algo == "Gaussian Mixture":
    labels = run_gmm(scaled, n_clusters)

elif algo == "Spectral":
    labels = run_spectral(scaled, n_clusters)

else:
    labels = run_meanshift(scaled)

pca = PCA(n_components=2)

components = pca.fit_transform(scaled)

plot_df = df.copy()
plot_df['Cluster'] = labels.astype(str)
plot_df['PCA1'] = components[:, 0]
plot_df['PCA2'] = components[:, 1]

fig = px.scatter(
    plot_df,
    x='PCA1',
    y='PCA2',
    color='Cluster',
    hover_name=plot_df.columns[0],
    size_max=20,
    title='Cluster Visualization (PCA)'
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Cluster Distribution")
st.bar_chart(plot_df['Cluster'].value_counts())
