import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Global Development AI Platform",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

with open("css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<div class='hero'>
<h1>🌍 GLOBAL DEVELOPMENT AI INTELLIGENCE PLATFORM</h1>
<p>Advanced Clustering Analytics & Economic Intelligence System</p>
</div>
""", unsafe_allow_html=True)

st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa", use_container_width=True)

st.markdown("## 🚀 Platform Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Countries", "190+")
col2.metric("Indicators", "45+")
col3.metric("Models", "6")
col4.metric("Accuracy", "95%")

st.markdown("---")

st.markdown("""
## 🌐 Features

- Interactive Clustering Lab
- AI Recommendation Engine
- Economic Intelligence Dashboard
- Real-Time Model Comparison
- Country Development Insights
- PCA / t-SNE / UMAP Visualizations
- Global Development Mapping
""")
