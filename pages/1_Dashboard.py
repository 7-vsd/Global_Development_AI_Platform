import streamlit as st
import plotly.express as px
import pandas as pd
from utils.data_loader import load_data

st.title("🌍 Global Development Dashboard")

file_path = "dataset/world_development_measurement.xlsx"
df = load_data(file_path)

col1, col2, col3 = st.columns(3)

col1.metric("Countries", df.shape[0])
col2.metric("Features", df.shape[1])
col3.metric("Missing Values", df.isnull().sum().sum())

numeric = df.select_dtypes(include='number')

fig = px.imshow(numeric.corr(),
                color_continuous_scale='RdBu_r',
                title='Correlation Heatmap')

st.plotly_chart(fig, use_container_width=True)
