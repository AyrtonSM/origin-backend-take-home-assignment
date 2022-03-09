import datetime
from src.main.util.enums.ValidationType import ValidationType
from src.main.util.enums.ScoreType import ScoreType
from src.main.util.enums.InsuranceType import InsuranceType
from src.main.util.RiskProfile import RiskProfile
from src.main.entity.User import User
from src.main.validation.Validator import Validator

""" UserRiskValidator is a class resposible for all types of validations in order to provide a validation to the business rules. 
    It also extends Validator which is an Abstract class containing validator() method signature. 
"""
class UserRiskValidator(Validator):

    def user_has_income(self,user : User) -> bool:
        """ Check if the user has some income """
        return user.get_income() > 0

    def user_is_over_60(self,user : User) -> bool:
        """ Check if the user is over 60 years old or not"""
        return user.get_age() > 60
    
    def user_is_under_30(self,user : User) -> bool:
        """ Check if the user is under 30 years old or not"""
        return user.get_age() < 30
    
    def user_is_between_30_40(self,user : User) -> bool:
        """ Check if the user is between 30 years old and 40 years old """
        return user.get_age() >= 30 and user.get_age() <= 40

    def user_income_is_above_200(self,user : User) -> bool:
        """ Check if the user has an income that is above $200.000 or not """
        return user.get_income() > 200000

    def user_house_is_mortgaged(self,user : User) -> bool:
        """ Check if the user's house is mortgaged if the user has one, if it doesn't, then returns False """
        house = user.get_house()
        status_key = 'ownership_status'
        if house != None and status_key in house:
            return house['ownership_status'] == "mortgaged"
        
        return False

    def user_has_dependents(self,user : User) -> bool:
        """ Check if the user has any dependents """
        return user.get_dependents() > 0 

    def user_is_married(self,user : User) -> bool:
        """ Check if the user is married """
        return user.get_marital_status() == "married" 
    
    def user_risk_questions_answered(self,user : User) -> bool:
        """ Check if the user answered the risk questions """
        return len(user.get_risk_question()) > 0

    def user_vehicle_produced_under_5_years(self,user : User) -> bool:
        """ Check if the user's auto was is less then 5 years old, if the user does not have an auto, then it returns False """
        vehicle = user.get_vehicle()
        if vehicle != None and "year" in vehicle:

            year = datetime.date.today().year
            difference = year - vehicle["year"] 
            return difference <= 5
        
        return False

    def validate(self, data) -> dict:
        """ Override method from class Validator, this method for this particular class 
        'UserRiskValidator' calculates the score of the user, based on its details.  """
        
        risk_profile = RiskProfile()
        score = risk_profile.get_base_score_map(data.get_risk_question())
        risk_profile_map = risk_profile.get_risk_profile_map()
        
        if not self.user_has_income(data):
            risk_profile_map[InsuranceType.DISABILITY] =  ScoreType.INELIGIBLE
        
        if self.user_is_over_60(data):
            risk_profile_map[InsuranceType.DISABILITY] =  ScoreType.INELIGIBLE
            risk_profile_map[InsuranceType.LIFE] =  ScoreType.INELIGIBLE
        
        if self.user_is_under_30(data):
            score[InsuranceType.AUTO] -= 2
            score[InsuranceType.DISABILITY] -= 2
            score[InsuranceType.HOME] -= 2
            score[InsuranceType.LIFE] -= 2

        if self.user_is_between_30_40(data):
            score[InsuranceType.AUTO] -= 1
            score[InsuranceType.DISABILITY] -= 1
            score[InsuranceType.HOME] -= 1
            score[InsuranceType.LIFE] -= 1

        
        if self.user_income_is_above_200(data):
            score[InsuranceType.AUTO] -= 1
            score[InsuranceType.DISABILITY] -= 1
            score[InsuranceType.HOME] -= 1
            score[InsuranceType.LIFE] -= 1


        if self.user_house_is_mortgaged(data):

            score[InsuranceType.DISABILITY] += 1
            score[InsuranceType.HOME] += 1


        if self.user_has_dependents(data):
            score[InsuranceType.DISABILITY] += 1
            score[InsuranceType.LIFE] += 1

        if self.user_is_married(data):
            score[InsuranceType.DISABILITY] -= 1
            score[InsuranceType.LIFE] += 1

        if self.user_vehicle_produced_under_5_years(data):
            score[InsuranceType.AUTO] += 1

        for key, val in risk_profile_map.items():
            if risk_profile_map[key] !=  ScoreType.INELIGIBLE:
                if score[key] <= 0: 
                    risk_profile_map[key] =  ScoreType.ECONOMIC
                elif score[key] == 1 or score[key] == 2 : 
                    risk_profile_map[key] =  ScoreType.REGULAR
                else:
                    risk_profile_map[key] =  ScoreType.RESPONSIBLE
        
        return risk_profile_map