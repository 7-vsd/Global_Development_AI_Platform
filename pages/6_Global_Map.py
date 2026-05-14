import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

st.title("🗺️ Global Development Map")

file_path = "dataset/world_development_measurement.xlsx"
df = load_data(file_path)

if 'Country' in df.columns:
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    selected_col = st.selectbox("Select Indicator", numeric_cols)

    fig = px.choropleth(
        df,
        locations='Country',
        locationmode='country names',
        color=selected_col,
        hover_name='Country',
        color_continuous_scale='Viridis',
        title=f'Global Map: {selected_col}'
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No 'Country' column found in the dataset.")
