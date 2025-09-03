import streamlit as st
import pandas as pd

st.title("🧭 Insights & Recommendations")

df = st.session_state.get("df_cache", pd.read_csv("route-optimization/logistics_deliveries.csv"))

late_by_city = df.groupby("city")["delivered_late"].mean().reset_index()
late_by_city["late_rate_%"] = (late_by_city["delivered_late"]*100).round(1)

st.subheader("Top Late Delivery Cities")
st.dataframe(late_by_city.sort_values("late_rate_%", ascending=False).head(10))

st.subheader("Recommendations")
st.write("""
- Add more vehicles in high-delay cities.  
- Prioritize critical orders during off-peak hours.  
- Use micro-depots closer to dense zones.  
- Upgrade routing algorithm to OR-Tools for production.
""")
