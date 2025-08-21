%%writefile app.py
import streamlit as st
import pickle
import numpy as np

st.title('Dynamic Fare Prediction App')

# Input field for distance
distance = st.number_input('Enter Trip Miles:', min_value=0.0, max_value=100.0, step=0.1)

# Predict button
if st.button('Predict Fare'):
    # Load the scaler and model
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    # Scale the input
    input_data = scaler.transform([[distance]])
    
    # Predict
    prediction = model.predict(input_data)
    
    # Display prediction
    st.write(f'Predicted Fare: ${prediction[0]:.2f}')
