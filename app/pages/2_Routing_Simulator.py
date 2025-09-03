import streamlit as st
import pandas as pd
import numpy as np
from math import radians, sin, cos, atan2

st.title("🗺️ Routing Simulator")

df = st.session_state.get("df_cache", pd.read_csv("route-optimization/logistics_deliveries.csv"))

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1))*cos(radians(lat2))*sin(dlon/2)**2
    return R * 2 * atan2(np.sqrt(a), np.sqrt(1-a))

date = st.selectbox("Order Date", sorted(df["order_date"].unique()))
day = df[df["order_date"] == date]

st.write(f"Deliveries for {date}: {len(day)}")
st.map(day[["customer_lat","customer_lon","depot_lat","depot_lon"]].rename(columns={
    "customer_lat":"lat", "customer_lon":"lon"
}))
