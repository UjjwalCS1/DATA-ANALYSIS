# app.py

import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("churn_model.pkl", "rb"))

st.title("Customer Churn Prediction")

st.write("Enter Customer Details")


# =========================
# INPUT FIELDS
# =========================

gender = st.selectbox("Gender", ["Female", "Male"])

SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])

Partner = st.selectbox("Partner", ["No", "Yes"])

Dependents = st.selectbox("Dependents", ["No", "Yes"])

tenure = st.slider("Tenure", 0, 72)

PhoneService = st.selectbox("Phone Service", ["No", "Yes"])

MultipleLines = st.selectbox(
    "Multiple Lines",
    ["No", "Yes", "No phone service"]
)

InternetService = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

OnlineSecurity = st.selectbox(
    "Online Security",
    ["No", "Yes", "No internet service"]
)

OnlineBackup = st.selectbox(
    "Online Backup",
    ["No", "Yes", "No internet service"]
)

DeviceProtection = st.selectbox(
    "Device Protection",
    ["No", "Yes", "No internet service"]
)

TechSupport = st.selectbox(
    "Tech Support",
    ["No", "Yes", "No internet service"]
)

StreamingTV = st.selectbox(
    "Streaming TV",
    ["No", "Yes", "No internet service"]
)

StreamingMovies = st.selectbox(
    "Streaming Movies",
    ["No", "Yes", "No internet service"]
)

Contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

PaperlessBilling = st.selectbox(
    "Paperless Billing",
    ["No", "Yes"]
)

PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

MonthlyCharges = st.number_input("Monthly Charges")

TotalCharges = st.number_input("Total Charges")


# =========================
# MANUAL ENCODING
# =========================

gender = 0 if gender == "Female" else 1

Partner = 0 if Partner == "No" else 1

Dependents = 0 if Dependents == "No" else 1

PhoneService = 0 if PhoneService == "No" else 1

PaperlessBilling = 0 if PaperlessBilling == "No" else 1


# MultipleLines
multiple_map = {
    "No": 0,
    "Yes": 1,
    "No phone service": 2
}
MultipleLines = multiple_map[MultipleLines]


# InternetService
internet_map = {
    "DSL": 0,
    "Fiber optic": 1,
    "No": 2
}
InternetService = internet_map[InternetService]


# Common mapping
common_map = {
    "No": 0,
    "Yes": 1,
    "No internet service": 2
}

OnlineSecurity = common_map[OnlineSecurity]
OnlineBackup = common_map[OnlineBackup]
DeviceProtection = common_map[DeviceProtection]
TechSupport = common_map[TechSupport]
StreamingTV = common_map[StreamingTV]
StreamingMovies = common_map[StreamingMovies]


# Contract
contract_map = {
    "Month-to-month": 0,
    "One year": 1,
    "Two year": 2
}
Contract = contract_map[Contract]


# Payment Method
payment_map = {
    "Electronic check": 0,
    "Mailed check": 1,
    "Bank transfer (automatic)": 2,
    "Credit card (automatic)": 3
}
PaymentMethod = payment_map[PaymentMethod]


# =========================
# PREDICTION
# =========================

if st.button("Predict"):

    input_data = np.array([[
        gender,
        SeniorCitizen,
        Partner,
        Dependents,
        tenure,
        PhoneService,
        MultipleLines,
        InternetService,
        OnlineSecurity,
        OnlineBackup,
        DeviceProtection,
        TechSupport,
        StreamingTV,
        StreamingMovies,
        Contract,
        PaperlessBilling,
        PaymentMethod,
        MonthlyCharges,
        TotalCharges
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Customer Will Churn")
    else:
        st.success("Customer Will Not Churn")