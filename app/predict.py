import json
import requests


url = "http://127.0.0.1:8000/ad_click_prediction"

input_data = {
    'age' : 26,
    'annual_salary' : 25000
}

input_json = json.dumps(input_data)
response = requests.post(url,data=input_json)
print(response.text)