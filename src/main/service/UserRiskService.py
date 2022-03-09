
from src.main.entity.User import User
from src.main.validation.UserRiskValidator import UserRiskValidator

"""
    UserRiskService is the service layer for dealing with User Risk, it holds methods to user risk evaluation 
"""
class UserRiskService:
    
    def __init__(self) -> None:
        pass
    
    def evaluate_user(self, user: User) -> dict:
        """ This method is responsible for connecting to the user risk validator and return a dictionary with the evaluation """
        user_validator = UserRiskValidator()
        return user_validator.validate(user)