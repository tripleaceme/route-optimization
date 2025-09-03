import streamlit as st
import pandas as pd

st.title("📊 Overview & Data Quality")

df = st.session_state.get("df_cache", pd.read_csv("route-optimization/logistics_deliveries.csv"))

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Deliveries", f"{len(df):,}")
col2.metric("Late Delivery Rate", f"{df['delivered_late'].mean()*100:.1f}%")
col3.metric("Avg Distance (km)", f"{df['distance_km_est'].mean():.1f}")
col4.metric("Avg Fuel Cost", f"{df['fuel_cost_est'].mean():.0f}")

st.dataframe(df.head(50))
