# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from app.predict import predict_default

app = FastAPI()

class RiskInput(BaseModel):
    credit_score: int
    loan_amount: int
    loan_term: int
    annual_income: int

@app.post("/predict")
def get_prediction(input_data: RiskInput):
    return predict_default(input_data.dict())
