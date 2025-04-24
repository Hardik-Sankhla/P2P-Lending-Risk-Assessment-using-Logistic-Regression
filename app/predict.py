# app/predict.py
import joblib
import numpy as np

model = joblib.load("model/logistic_model.pkl")
scaler = joblib.load("model/scaler.pkl")

def predict_default(data):
    features = np.array([[data['credit_score'], data['loan_amount'], data['loan_term'], data['annual_income']]])
    scaled = scaler.transform(features)
    prob = model.predict_proba(scaled)[0][1]
    prediction = model.predict(scaled)[0]
    return {
        "probability": round(prob, 4),
        "prediction": int(prediction),
        "risk": "High Risk" if prediction == 1 else "Low Risk"
    }
