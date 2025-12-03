from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

model = joblib.load('bank_churn_model.joblib')

class Customer(BaseModel):
    CreditScore: int
    Geography: str
    Gender: str
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float

app = FastAPI()

def preprocess(data: pd.DataFrame):
    df = data.copy()
    df['Gender_Male'] = df['Gender'].apply(lambda x: 1 if x == 'Male' else 0)
    df['Geography_Germany'] = df['Geography'].apply(lambda x: 1 if x == 'Germany' else 0)
    df['Geography_Spain'] = df['Geography'].apply(lambda x: 1 if x == 'Spain' else 0)
    df = df.drop(columns=['Geography', 'Gender'])
    
    expected_cols = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 
                     'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 
                     'Geography_Germany', 'Geography_Spain', 'Gender_Male']
    return df[expected_cols]

@app.get("/")
def home():
    return {"message": "Bank Churn API (Pro Structure)"}

@app.post("/predict")
def predict_churn(customer: Customer):
    input_df = pd.DataFrame([customer.dict()])
    processed_df = preprocess(input_df)
    
    # Threshold 0.4
    probability = model.predict_proba(processed_df)[0][1]
    
    if probability >= 0.40:
        result = "CHURN Risk ⚠️"
    else:
        result = "Safe ✅"
    
    return {
        "result": result,
        "churn_probability": f"{probability * 100:.2f}%"
    }