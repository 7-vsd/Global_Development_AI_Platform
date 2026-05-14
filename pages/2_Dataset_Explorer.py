import streamlit as st
import pandas as pd
from utils.data_loader import load_data

st.title("📊 Dataset Explorer")

uploaded = st.file_uploader("Upload Dataset", type=['xlsx', 'csv'])

if uploaded:
    if uploaded.name.endswith('csv'):
        df = pd.read_csv(uploaded)
    else:
        df = pd.read_excel(uploaded)
else:
    df = load_data("dataset/world_development_measurement.xlsx")

st.dataframe(df, use_container_width=True)

st.subheader("Missing Values")
st.write(df.isnull().sum())

st.subheader("Statistics")
st.write(df.describe())
