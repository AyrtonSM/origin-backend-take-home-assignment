class User:
    def __init__(self, age, dependents, house, income, marital_status, risk_question, vehicle): 
        
        self.__age = age
        self.__dependents = dependents
        self.__house = house
        self.__income = income
        self.__marital_status = marital_status
        self.__risk_question = risk_question
        self.__vehicle = vehicle
    
    def get_age(self):
        return self.__age

    def get_dependents(self):
        return self.__dependents

    def get_house(self):
        return self.__house

    def get_income(self):
        return self.__income

    def get_marital_status(self):
        return self.__marital_status

    def get_risk_question(self):
        return self.__risk_question

    def get_vehicle(self):
        return self.__vehicle
    