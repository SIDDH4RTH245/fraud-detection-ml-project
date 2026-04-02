import streamlit as st
import pandas as pd
import joblib
import os

# Get path to model relative to this file
model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'fraud_model.pkl')
model = joblib.load(model_path)

st.title("💳 Fraud Detection App")

st.write("Enter transaction details")

amount = st.number_input("Transaction Amount", 0.0, 100000.0, 100.0)

# The model expects 30 features: Time, V1-V28, and Amount.
# We use default 0.0 for Time and V1-V28, and use the user's input for Amount.
input_dict = {"Time": 0.0}
for i in range(1, 29):
    input_dict[f"V{i}"] = 0.0
input_dict["Amount"] = amount

input_data = pd.DataFrame([input_dict])

if st.button("Check Fraud"):
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction")
    else:
        st.success("✅ Legitimate Transaction")