from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
from utils import scale,classify,load_model

app = FastAPI()

class model_input(BaseModel):

    age:int
    annual_salary:int

# loading_fitted_scaler
scaler = load_model('min_max_scaler_model.p')
# loading_trained_model
model = load_model('logistic_regression_model.p')

@app.post('/ad_click_prediction')
def ad_click_pred(input_parameters : model_input):

    age = input_parameters.age
    annual_salary = input_parameters.annual_salary

    user_input = [age,annual_salary]
    scaled_data = scale(user_input,scaler)
    results = classify(scaled_data,model)
    
    if results is not None: 
        return f"Result : {results['classification']}, Confidence_Score : {results['score']:.2f}"
    return "Error!"


# to get local-host api url, run in cmd : uvicorn main:app