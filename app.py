
import streamlit as st
import pickle as pkl
import pandas as pd

with open("MLR.pickle", "rb") as f:
  s_model = pkl.load(f)

st.title("House Price Prediction")
area_sqft = st.number_input("Area_sqft", min_value=0.0, max_value=20000.0, step=10.0)
bedrooms = st.number_input("Bedrooms", min_value=0, max_value=10, step=1.0)
bathrooms = st.number_input("Bathrooms", min_value=0, max_value=10, step=1.0)
age_years = st.number_input("Age of House (year)", min_value=0.0, max_value=100.0, step=1.0)
distance = st.number_input("Distance to city km", min_value=0.0, max_value=100.0, step=0.5)

if st.button("Predict House Price"):
  input_df = pd.DataFrame([[area_sqft, bedrooms, bathrooms, age_years, distance]], columns=["Area_sqft", "Bedrooms", "Bathrooms", "Age_years", "Distance_to_city_km"])
  prediction = s_model.predict(input_df)
  st.success(f"Predicted House Price: {prediction[0]:.2f} Rupees")
  
