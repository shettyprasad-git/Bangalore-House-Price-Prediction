import streamlit as st
import pickle
import json
import numpy as np

# Load model
with open('banglore_home_prices_model.pickle', 'rb') as f:
    model = pickle.load(f)

# Load columns
with open('columns.json', 'r') as f:
    data_columns = json.load(f)['data_columns']

# Extract locations (after numeric columns)
locations = data_columns[4:]

# App title
st.title("🏠 Bangalore House Price Prediction")
st.write("Predict house prices based on location and property details")

# User inputs
location = st.selectbox("Select Location", locations)
sqft = st.number_input("Total Square Feet", min_value=300.0, step=50.0)
bath = st.number_input("Number of Bathrooms", min_value=1, step=1)
balcony = st.number_input("Number of Balconies", min_value=0, step=1)
bhk = st.number_input("BHK", min_value=1, step=1)

# Predict button
if st.button("Predict Price"):
    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = balcony
    x[3] = bhk

    if location in data_columns:
        loc_index = data_columns.index(location)
        x[loc_index] = 1

    price = model.predict([x])[0]

    st.success(f"💰 Estimated Price: ₹ {round(price, 2)} Lakhs")
