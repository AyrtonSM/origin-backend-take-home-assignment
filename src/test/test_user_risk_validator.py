import sys
import os
sys.path.insert(0,os.path.realpath(__name__ + "/../../../"))

import unittest
from src.main.entity.User import User
from src.main.validation.UserRiskValidator import UserRiskValidator

class TestUserRiskValidator(unittest.TestCase):

    def test_user_does_not_have_income(self):
        user = User(age=35,
                    dependents=2,
                    house= {"ownership_status": "owned"},
                    income = 0,
                    marital_status = "married",
                    risk_question = [0, 1, 0],
                    vehicle = {"year": 2018})

        validator = UserRiskValidator()
        data = validator.validate(user)
        self.assertEqual(data["auto"], "regular")
        self.assertEqual(data["disability"], "ineligible")
        self.assertEqual(data["home"] , "economic")
        self.assertEqual(data["life"] , "regular")
    
    def test_user_is_over_60(self):
        user = User(age=61,
                    dependents=2,
                    house= {"ownership_status": "owned"},
                    income = 0,
                    marital_status = "single",
                    risk_question = [0, 1, 0],
                    vehicle = {"year": 2019})

        validator = UserRiskValidator()
        data = validator.validate(user)
        self.assertEqual(data["disability"], "ineligible")
        self.assertEqual(data["life"] , "ineligible")

    def test_user_is_under_30(self):
        user = User(age=21,
                    dependents=2,
                    house= {"ownership_status": "owned"},
                    income = 0,
                    marital_status = "single",
                    risk_question = [0, 1, 0],
                    vehicle = {"year": 2019})

        validator = UserRiskValidator()
        data = validator.user_is_under_30(user)
        self.assertTrue(data)

    def test_user_is_not_under_30(self):
        user = User(age=41,
                    dependents=2,
                    house= {"ownership_status": "owned"},
                    income = 0,
                    marital_status = "single",
                    risk_question = [0, 1, 0],
                    vehicle = {"year": 2019})

        validator = UserRiskValidator()
        data = validator.user_is_under_30(user)
        self.assertFalse(data)

    def test_user_house_is_mortgaged(self):
        user = User(age=41,
                    dependents=2,
                    house= {"ownership_status": "mortgaged"},
                    income = 0,
                    marital_status = "single",
                    risk_question = [0, 1, 0],
                    vehicle = {"year": 2019})

        validator = UserRiskValidator()
        data = validator.user_house_is_mortgaged(user)
        self.assertTrue(data)

    def test_user_house_is_not_mortgaged(self):
        user = User(age=41,
                    dependents=2,
                    house= {"ownership_status": "owned"},
                    income = 0,
                    marital_status = "single",
                    risk_question = [0, 1, 0],
                    vehicle = {"year": 2019})

        validator = UserRiskValidator()
        data = validator.user_house_is_mortgaged(user)
        self.assertFalse(data)
    
    def test_user_house_is_owned(self):
        user = User(age=41,
                    dependents=2,
                    house= {"ownership_status": "owned"},
                    income = 0,
                    marital_status = "single",
                    risk_question = [0, 1, 0],
                    vehicle = {"year": 2019})

        validator = UserRiskValidator()
        data = validator.user_house_is_mortgaged(user)
        self.assertFalse(data)

    def test_user_house_is_not_owned(self):
        user = User(age=41,
                    dependents=2,
                    house= {"ownership_status": "mortgaged"},
                    income = 0,
                    marital_status = "single",
                    risk_question = [0, 1, 0],
                    vehicle = {"year": 2019})

        validator = UserRiskValidator()
        data = validator.user_house_is_mortgaged(user)
        self.assertTrue(data)

    def test_user_has_dependents(self):
        user = User(age=41,
                    dependents=2,
                    house= {"ownership_status": "owned"},
                    income = 0,
                    marital_status = "single",
                    risk_question = [0, 1, 0],
                    vehicle = {"year": 2019})

        validator = UserRiskValidator()
        data = validator.user_has_dependents(user)
        self.assertTrue(data)
    
    def test_user_does_not_have_dependents(self):
        user = User(age=41,
                    dependents=-2,
                    house= {"ownership_status": "owned"},
                    income = 0,
                    marital_status = "single",
                    risk_question = [0, 1, 0],
                    vehicle = {"year": 2019})

        validator = UserRiskValidator()
        data = validator.user_has_dependents(user)
        self.assertFalse(data)

    def test_user_is_married(self):
        user = User(age=41,
                    dependents=-2,
                    house= {"ownership_status": "owned"},
                    income = 0,
                    marital_status = "married",
                    risk_question = [0, 1, 0],
                    vehicle = {"year": 2019})

        validator = UserRiskValidator()
        data = validator.user_is_married(user)
        self.assertTrue(data)

    def test_user_is_not_married(self):
        user = User(age=41,
                    dependents=-2,
                    house= {"ownership_status": "owned"},
                    income = 0,
                    marital_status = "single",
                    risk_question = [0, 1, 0],
                    vehicle = {"year": 2019})

        validator = UserRiskValidator()
        data = validator.user_is_married(user)
        self.assertFalse(data)
    
    def test_user_vehicle_produced_under_5_years(self):
        user = User(age=41,
                    dependents=-2,
                    house= {"ownership_status": "owned"},
                    income = 0,
                    marital_status = "single",
                    risk_question = [0, 1, 0],
                    vehicle = {"year": 2019})

        validator = UserRiskValidator()
        data = validator.user_vehicle_produced_under_5_years(user)
        self.assertTrue(data)

    def test_user_vehicle_not_produced_under_5_years(self):
        user = User(age=41,
                    dependents=-2,
                    house= {"ownership_status": "owned"},
                    income = 0,
                    marital_status = "single",
                    risk_question = [0, 1, 0],
                    vehicle = {"year": 1999})

        validator = UserRiskValidator()
        data = validator.user_vehicle_produced_under_5_years(user)
        self.assertFalse(data)
    
    def test_user_questions_answered(self):
        user = User(age=41,
                    dependents=-2,
                    house= {"ownership_status": "owned"},
                    income = 0,
                    marital_status = "single",
                    risk_question = [0, 1, 0],
                    vehicle = {"year": 1999})

        validator = UserRiskValidator()
        data = validator.user_risk_questions_answered(user)
        self.assertTrue(data)

    def test_user_questions_not_answered(self):
        user = User(age=41,
                    dependents=-2,
                    house= {"ownership_status": "owned"},
                    income = 0,
                    marital_status = "single",
                    risk_question = [],
                    vehicle = {"year": 1999})

        validator = UserRiskValidator()
        data = validator.user_risk_questions_answered(user)
        self.assertFalse(data, "Risk questions must be answered")
    
    def test_user(self):
        user = User(age=20,
                    dependents=-2,
                    house= {"ownership_status": "owned"},
                    income = 0,
                    marital_status = "single",
                    risk_question = [0, 1, 0],
                    vehicle = {"year": 1999})

        validator = UserRiskValidator()
        data = validator.user_vehicle_produced_under_5_years(user)
        self.assertFalse(data)
        
    

if __name__ == "__name__":
    unittest.main()