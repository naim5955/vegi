import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")
st.title("🌿 Vegetation Monitoring (False Color)")

# Sidebar inputs
with st.sidebar:
    st.header("User Input")
    lat = st.number_input("Latitude", value=23.8103, format="%.6f")
    lon = st.number_input("Longitude", value=90.4125, format="%.6f")
    year = st.selectbox("Select Year", list(range(2016, 2025)))
    radius_km = st.slider("Radius (km)", 1, 20, 5)

# Create map
m = leafmap.Map(center=(lat, lon), zoom=10)

# Create tile URL from Microsoft Planetary Computer Sentinel-2 Layer
tile_url = (
    f"https://services.digitalglobe.com/earthservice/sentinel-2?"
    f"lat={lat}&lon={lon}&year={year}"
)

# Use a fixed Sentinel-2 false color tile layer (from Microsoft)
sentinel_tile = (
    "https://services.sentinel-hub.com/ogc/wms/"
    "sentinel-2-l2a?"
    "layers=FALSE-COLOR&maxcc=0.2&gain=1.4&"
    f"TIME={year}-01-01/{year}-12-31&"
    f"WIDTH=512&HEIGHT=512&FORMAT=image/png&"
    "bbox={bbox}"
)

# Add Sentinel-2 tile layer from Microsoft Planetary Computer
m.add_tile_layer(
    url="https://tiles.macrostrat.org/sentinel-2/false-color/{z}/{x}/{y}.png",
    name="False Color (Sentinel-2)",
    attribution="Microsoft Planetary Computer",
    opacity=1.0
)

# Add marker for user-selected point
m.add_marker(location=[lat, lon], popup="Selected Location")

m.to_streamlit(height=700)

st.markdown("🔍 This view shows near-infrared (NIR) as red — healthy vegetation looks bright red.")
