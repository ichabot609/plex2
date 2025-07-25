# streamlit_app.py
# Interface Streamlit pour visualiser les plex

import streamlit as st
import pandas as pd

st.title("Analyse de rentabilité - Plex à Québec")

try:
    df = pd.read_csv("data/annonces.csv")
    st.dataframe(df)
except FileNotFoundError:
    st.warning("Aucune donnée disponible.")
