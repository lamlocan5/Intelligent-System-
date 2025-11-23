
#B22DCCN476 - Đỗ Ngọc Lâm

import numpy as np
import streamlit as st
import tensorflow as tf
import joblib

st.title("Diabetes Prediction Web App (Best Model)")

st.write("Nhập các thông số (Pima Indians Diabetes) để dự đoán nguy cơ mắc tiểu đường.")

# Load best model & scaler
model = tf.keras.models.load_model("diabetes_model_best.h5")
scaler = joblib.load("diabetes_scaler.pkl")

# Input features
pregnancies = st.number_input("Pregnancies (số lần mang thai)", min_value=0.0, max_value=20.0, value=1.0, step=1.0)
glucose = st.number_input("Glucose (plasma glucose concentration)", min_value=0.0, max_value=300.0, value=120.0, step=1.0)
blood_pressure = st.number_input("BloodPressure (mm Hg)", min_value=0.0, max_value=200.0, value=70.0, step=1.0)
skin_thickness = st.number_input("SkinThickness (mm)", min_value=0.0, max_value=100.0, value=20.0, step=1.0)
insulin = st.number_input("Insulin (2-Hour serum insulin mu U/ml)", min_value=0.0, max_value=900.0, value=80.0, step=1.0)
bmi = st.number_input("BMI (kg/(m^2))", min_value=0.0, max_value=70.0, value=25.0, step=0.1)
dpf = st.number_input("DiabetesPedigreeFunction", min_value=0.0, max_value=3.0, value=0.5, step=0.01)
age = st.number_input("Age (years)", min_value=0.0, max_value=120.0, value=33.0, step=1.0)

if st.button("Predict"):
    x = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                   insulin, bmi, dpf, age]], dtype=float)
    x_scaled = scaler.transform(x)
    prob = model.predict(x_scaled)[0, 0]
    label = int(prob >= 0.5)

    st.write(f"Xác suất mắc tiểu đường: **{prob:.3f}**")
    if label == 1:
        st.error("Dự đoán: **Diabetic (1)**")
    else:
        st.success("Dự đoán: **Non-diabetic (0)**")
