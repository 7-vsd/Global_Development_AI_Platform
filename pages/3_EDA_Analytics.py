import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

st.title("📈 EDA Analytics Center")

file_path = "dataset/world_development_measurement.xlsx"
df = load_data(file_path)

numeric_cols = df.select_dtypes(include='number').columns.tolist()

selected = st.selectbox("Select Feature", numeric_cols)

fig = px.histogram(df, x=selected, nbins=30,
                   color_discrete_sequence=['cyan'])

st.plotly_chart(fig, use_container_width=True)

fig2 = px.box(df, y=selected)

st.plotly_chart(fig2, use_container_width=True)
