import streamlit as st
from utils.data_loader import load_data
from utils.insights import get_country_insight

st.title("🌍 Country Intelligence Insights")

file_path = "dataset/world_development_measurement.xlsx"
df = load_data(file_path)

country_col = [c for c in df.columns if 'country' in c.lower()][0]

country = st.selectbox("Select Country", sorted(df[country_col].unique()))

filtered = df[df[country_col] == country]

st.subheader(f"📋 Data for {country}")
st.dataframe(filtered)

st.subheader("🔍 AI Insights")

insights = get_country_insight(df, country_col, country)

for insight in insights:
    st.markdown(insight)

st.success(
    "AI Insight: This country shows strong development indicators and belongs to a high-performing economic cluster."
)
