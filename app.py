import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer

# Adapter la page
st.set_page_config(
    page_title="DataViz",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load data
uploaded_file = st.file_uploader("Choisir un fichier CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    pyg_app = StreamlitRenderer(df)
    pyg_app.explorer()
