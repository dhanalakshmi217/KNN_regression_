import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("🩺 Diabetes Prediction App")

preg = st.number_input("Pregnancies", min_value=0)
glu = st.number_input("Glucose", min_value=0)
bp = st.number_input("Blood Pressure", min_value=0)
skin = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=1)

if st.button("Predict"):
    input_data = np.array([[
        preg, glu, bp, skin, insulin, bmi, dpf, age
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("❌ Diabetes Detected")
    else:
        st.success("✅ No Diabetes")
