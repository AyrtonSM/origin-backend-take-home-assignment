import sys
import os
sys.path.insert(0, os.getcwd())

from flask import Flask, request
from src.main.entity.User import User
from src.main.service.UserRiskService import UserRiskService

app = Flask(__name__)

@app.route('/')
def index():
    return "Origin Backend Take-Home Assignment"

@app.route('/risk-analysis', methods=['POST'])
def risk_analysis():

    if request.content_type != 'application/json':
        return app.make_response(('Invalid content-type. Must be application/json.', 500))

    user_details = request.json

    try:
        user = User(age = user_details['age'], 
                    dependents = user_details['dependents'],
                    house=user_details['house'], 
                    income=user_details['income'], 
                    marital_status = user_details['marital_status'], 
                    risk_question=user_details['risk_questions'], 
                    vehicle=user_details['vehicle'])

        user_risk_service = UserRiskService()

        result = user_risk_service.evaluate_user(user)
        return app.make_response((result, 200))

    except KeyError:
        return app.make_response(("An error has occoured, please verify if all values are set properly", 500))


app.run('0.0.0.0', 5000)