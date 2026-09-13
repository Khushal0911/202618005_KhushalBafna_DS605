import streamlit as st
import requests

# Replace with your deployed Vercel URL
API_URL = "https://your-vercel-app-name.vercel.app/predict"

st.title("🏡 Airbnb Nightly Price Predictor")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    with col1:
        neighbourhood_group = st.selectbox("Borough", ["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"])
        room_type = st.selectbox("Room Type", ["Entire home/apt", "Private room", "Shared room"])
        minimum_nights = st.number_input("Minimum Nights", min_value=1, value=1)
        availability_365 = st.number_input("Availability (Days/Year)", min_value=0, max_value=365, value=150)
        
    with col2:
        number_of_reviews = st.number_input("Total Reviews", min_value=0, value=10)
        reviews_per_month = st.number_input("Reviews Per Month", min_value=0.0, value=1.0)
        calculated_host_listings_count = st.number_input("Host Listings Count", min_value=1, value=1)
        latitude = st.number_input("Latitude", value=40.7128, format="%.4f")
        longitude = st.number_input("Longitude", value=-74.0060, format="%.4f")
        
    submit = st.form_submit_button("Estimate Price")

if submit:
    payload = {
        "neighbourhood_group": neighbourhood_group,
        "room_type": room_type,
        "minimum_nights": minimum_nights,
        "number_of_reviews": number_of_reviews,
        "reviews_per_month": reviews_per_month,
        "calculated_host_listings_count": calculated_host_listings_count,
        "availability_365": availability_365,
        "neighbourhood_freq": 0.015, # Hardcoded median for simplicity 
        "latitude": latitude,
        "longitude": longitude
    }
    
    with st.spinner("Calculating..."):
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            price = response.json()["predicted_price"]
            st.success(f"### Estimated Nightly Price: ${price:.2f}")
        else:
            st.error("Error communicating with the API.")