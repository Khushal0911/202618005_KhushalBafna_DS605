import streamlit as st
import requests

st.set_page_config(page_title="NYC Airbnb Price Estimator", page_icon="🗽", layout="centered")

BOROUGH_METADATA = {
    "Manhattan": {"lat": 40.7831, "lon": -73.9712, "freq": 0.44},
    "Brooklyn": {"lat": 40.6782, "lon": -73.9442, "freq": 0.41},
    "Queens": {"lat": 40.7282, "lon": -73.7949, "freq": 0.11},
    "Bronx": {"lat": 40.8448, "lon": -73.8648, "freq": 0.02},
    "Staten Island": {"lat": 40.5795, "lon": -74.1502, "freq": 0.01}
}

API_URL = "https://two02618005-khushalbafna-ds605-1.onrender.com/predict"

st.title("🗽 NYC Airbnb Price Estimator")
st.markdown("Enter your listing details below for an AI-powered nightly price recommendation.")

# Top-level placeholder for results so mobile users don't have to scroll down
result_placeholder = st.empty()

with st.form("pricing_form"):
    st.subheader("📍 Property Details")
    col1, col2 = st.columns(2)
    
    with col1:
        neighbourhood_group = st.selectbox(
            "Borough", 
            options=list(BOROUGH_METADATA.keys()),
            help="Select the New York City borough where the property is located."
        )
        room_type = st.selectbox(
            "Room Type", 
            options=["Entire home/apt", "Private room", "Shared room"]
        )
        calculated_host_listings_count = st.number_input(
            "Total Listings You Host", 
            min_value=1, max_value=50, value=1
        )

    with col2:
        minimum_nights = st.slider("Minimum Nights Required", 1, 30, 2)
        availability_365 = st.slider("Availability (Days per Year)", 0, 365, 180)
    
    st.divider()
    st.subheader("⭐ Review Metrics")
    col3, col4 = st.columns(2)
    
    with col3:
        number_of_reviews = st.number_input(
            "Total Number of Reviews", 
            min_value=0, max_value=1000, value=10, step=5
        )
    with col4:
        reviews_per_month = st.slider(
            "Average Reviews per Month", 
            0.0, 10.0, 1.0, step=0.1
        )

    submitted = st.form_submit_button("💡 Get Price Estimate", use_container_width=True)

if submitted:
    selected_meta = BOROUGH_METADATA[neighbourhood_group]
    
    payload = {
        "neighbourhood_group": neighbourhood_group,
        "room_type": room_type,
        "minimum_nights": minimum_nights,
        "number_of_reviews": number_of_reviews,
        "reviews_per_month": reviews_per_month,
        "calculated_host_listings_count": calculated_host_listings_count,
        "availability_365": availability_365,
        "neighbourhood_freq": selected_meta["freq"],
        "latitude": selected_meta["lat"],
        "longitude": selected_meta["lon"]
    }
    
    with st.spinner("Calculating optimal price..."):
        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                price = response.json()["predicted_price"]
                
                # Render the success message and metric inside the top placeholder
                with result_placeholder.container():
                    st.success("Analysis Complete!")
                    st.metric(label=f"Recommended Rate: {room_type} in {neighbourhood_group}", value=f"${price:.2f}")
            else:
                result_placeholder.error(f"API Error: {response.status_code}")
        except Exception as e:
            result_placeholder.error("Failed to connect to the prediction server. Ensure the backend is live.")