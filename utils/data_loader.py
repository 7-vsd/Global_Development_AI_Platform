import pandas as pd
import streamlit as st

@st.cache_data
def load_data(path):
    df = pd.read_excel(path)
    return df
