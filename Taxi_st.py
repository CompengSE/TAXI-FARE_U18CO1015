import joblib
import streamlit as st
import numpy as np

loaded_model = joblib.load('random_forest_model.pkl')

st.title("TAXI_FARE PREDICTOR")
pickup_Long = st.number_input("Pickup longitude: ")
pickup_Lat = st.number_input("Pickup Latitude: ")
Dropoff_Long = st.number_input("Dropoff Longitude: ")
Dropoff_Lat = st.number_input("Dropoff Latitude: ")
Passenger = st.number_input("Passenger count: ")

button = st.button("Predict")
if button:
    x = np.array([[pickup_Long, pickup_Lat, Dropoff_Long, Dropoff_Lat, Passenger]])
    y = loaded_model.predict(x)
    st.subheader(f"Predicted Fare: ${y[0]:.2f}")
