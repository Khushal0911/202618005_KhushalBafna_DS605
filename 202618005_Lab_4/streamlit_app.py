import streamlit as st
import requests

st.set_page_config(
    page_title="NYC Airbnb Price Estimator",
    page_icon="🗽",
    layout="wide"
)

# Custom pastel styling
st.markdown("""
<style>
    /* Main app background & font colors */
    .stApp {
        background-color: #F8FAFC;
        color: #334155;
    }
    
    /* Pastel card container for results */
    .pastel-card {
        background: linear-gradient(135deg, #F0F4FF 0%, #E8EEF5 100%);
        border: 1px solid #D9E2EC;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 16px rgba(148, 163, 184, 0.12);
        margin-bottom: 16px;
    }
    
    .pastel-placeholder {
        background-color: #F1F5F9;
        border: 2px dashed #CBD5E1;
        border-radius: 16px;
        padding: 40px 24px;
        text-align: center;
        color: #64748B;
    }

    .price-tag {
        font-size: 2.75rem;
        font-weight: 700;
        color: #4F46E5;
        margin: 8px 0;
    }

    /* Form button pastel accent */
    div.stButton > button:first-child {
        background-color: #818CF8;
        color: white;
        border: none;
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.2s ease-in-out;
    }
    div.stButton > button:first-child:hover {
        background-color: #6366F1;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

BOROUGH_METADATA = {
    "Manhattan": {"lat": 40.7831, "lon": -73.9712, "freq": 0.44},
    "Brooklyn": {"lat": 40.6782, "lon": -73.9442, "freq": 0.41},
    "Queens": {"lat": 40.7282, "lon": -73.7949, "freq": 0.11},
    "Bronx": {"lat": 40.8448, "lon": -73.8648, "freq": 0.02},
    "Staten Island": {"lat": 40.5795, "lon": -74.1502, "freq": 0.01}
}

API_URL = "https://two02618005-khushalbafna-ds605-1.onrender.com/predict"

st.title("🗽 NYC Airbnb Price Estimator")
st.caption("AI-powered nightly valuation engine trained on New York City rental telemetry.")

# Split view: Form on the left, live output panel on the right
left_col, right_col = st.columns([1.1, 0.9], gap="large")

with left_col:
    with st.form("pricing_form"):
        st.subheader("📍 Property Details")
        f_col1, f_col2 = st.columns(2)
        with f_col1:
            neighbourhood_group = st.selectbox(
                "Borough", 
                options=list(BOROUGH_METADATA.keys())
            )
            room_type = st.selectbox(
                "Room Type", 
                options=["Entire home/apt", "Private room", "Shared room"]
            )
            calculated_host_listings_count = st.number_input(
                "Host Listings Count", 
                min_value=1, max_value=50, value=1
            )
        with f_col2:
            minimum_nights = st.slider("Min Nights", 1, 30, 2)
            availability_365 = st.slider("Availability (Days/Year)", 0, 365, 180)

        st.divider()
        st.subheader("⭐ Review Metrics")
        f_col3, f_col4 = st.columns(2)
        with f_col3:
            number_of_reviews = st.number_input(
                "Total Reviews", 
                min_value=0, max_value=1000, value=10, step=5
            )
        with f_col4:
            reviews_per_month = st.slider(
                "Reviews / Month", 
                0.0, 10.0, 1.0, step=0.1
            )

        submitted = st.form_submit_button("💡 Get Price Estimate", use_container_width=True)

with right_col:
    st.subheader("📊 Valuation Summary")
    
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
        
        with st.spinner("Querying backend inference service..."):
            try:
                response = requests.post(API_URL, json=payload, timeout=15)
                if response.status_code == 200:
                    price = response.json()["predicted_price"]
                    
                    st.markdown(f"""
                    <div class="pastel-card">
                        <span style="color: #6366F1; font-weight: 600; text-transform: uppercase; font-size: 0.8rem; letter-spacing: 0.05em;">Recommended Nightly Rate</span>
                        <div class="price-tag">${price:.2f}</div>
                        <p style="margin: 0; color: #475569; font-size: 0.95rem;">
                            Estimated fair market rate for an <strong>{room_type}</strong> in <strong>{neighbourhood_group}</strong>.
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown("**Listing Snapshot:**")
                    st.write(f"• **Stay Requirement:** {minimum_nights} nights minimum")
                    st.write(f"• **Listing Density:** {availability_365} open days / year")
                    st.write(f"• **Review Velocity:** {reviews_per_month} reviews / month ({number_of_reviews} total)")
                else:
                    st.error(f"API Error {response.status_code}: Unable to compute rate.")
            except requests.exceptions.RequestException:
                st.error("Server timeout or unreachable backend. Please check the Render service status.")
    else:
        st.markdown("""
        <div class="pastel-placeholder">
            <h4 style="color: #475569; margin-bottom: 6px;">Awaiting Input</h4>
            <p style="font-size: 0.9rem; margin: 0;">Adjust listing attributes on the left and submit to view the real-time valuation card here.</p>
        </div>
        """, unsafe_allow_html=True)