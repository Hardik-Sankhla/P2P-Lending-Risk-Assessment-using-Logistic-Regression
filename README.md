# Peer-to-Peer(P2P) Lending Risk Assessment
___

#### This project predicts the probability of a borrower defaulting on a peer-to-peer loan.
___

# Description:
In peer-to-peer (P2P) lending, individuals lend money to other individuals through an online platform. The risk assessment involves predicting the likelihood of a borrower defaulting on the loan based on their financial profile, credit score, loan amount, and loan term. In this project, we will build a predictive model using Logistic Regression to assess the risk of loan default.

___

## Features
- Logistic Regression Model
- FastAPI Backend
- Streamlit Frontend
 
___

## Run Locally

```bash
git clone https://github.com/your-username/p2p-lending-risk.git
cd p2p-lending-risk
pip install -r requirements.txt

# Run the web app
streamlit run streamlit_app.py

# Run the API
uvicorn app.main:app --reload
```