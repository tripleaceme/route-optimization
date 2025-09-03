import os
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(page_title="Logistics Route Optimization", layout="wide")
st.title("📦 Logistics Route Optimization – Demo")

df = pd.read_csv("route-optimization/logistics_deliveries.csv")

st.session_state["df_cache"] = df

st.dataframe(df.head())
st.markdown("Navigate with sidebar to view analysis pages.")
