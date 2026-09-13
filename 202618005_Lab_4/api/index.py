from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
import os

app = FastAPI()

# Dynamically resolve root path where .pkl files are stored
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'best_airbnb_model.pkl')
FEATURES_PATH = os.path.join(BASE_DIR, 'model_features.pkl')

# Load model and feature columns
model = joblib.load(MODEL_PATH)
features = joblib.load(FEATURES_PATH)

# Define the expected JSON payload
class ListingData(BaseModel):
    minimum_nights: int
    number_of_reviews: int
    reviews_per_month: float
    calculated_host_listings_count: int
    availability_365: int
    neighbourhood_freq: float
    latitude: float
    longitude: float
    neighbourhood_group: str
    room_type: str

@app.get("/")
def read_root():
    return {"status": "success", "message": "Airbnb Price Prediction API is live!"}

@app.post("/predict")
def predict_price(data: ListingData):
    # Convert input to DataFrame (Pydantic v2 compatibility)
    df = pd.DataFrame([data.model_dump()])
    
    # Apply one-hot encoding for categorical variables
    df = pd.get_dummies(df, columns=['neighbourhood_group', 'room_type'])
    
    # Reindex to match the exact feature columns the model was trained on
    df = df.reindex(columns=features, fill_value=0)
    
    # Predict and reverse the log1p transformation
    log_price_pred = model.predict(df)[0]
    estimated_price = np.expm1(log_price_pred)
    
    return {"predicted_price": float(estimated_price)}