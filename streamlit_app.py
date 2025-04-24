# streamlit_app.py
import streamlit as st
from app.predict import predict_default

st.title("P2P Lending Risk Assessment")

credit_score = st.slider("Credit Score", 600, 850, 700)
loan_amount = st.number_input("Loan Amount ($)", min_value=1000, max_value=50000, value=15000)
loan_term = st.selectbox("Loan Term (months)", [12, 24, 36, 48, 60])
annual_income = st.number_input("Annual Income ($)", min_value=20000, max_value=100000, value=55000)

if st.button("Assess Risk"):
    input_data = {
        "credit_score": credit_score,
        "loan_amount": loan_amount,
        "loan_term": loan_term,
        "annual_income": annual_income
    }
    result = predict_default(input_data)
    st.write("### Risk Prediction")
    st.write(f"**Probability of Default:** {result['probability']}")
    st.write(f"**Prediction:** {result['risk']}")
