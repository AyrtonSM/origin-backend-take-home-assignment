from src.main.util.enums.InsuranceType import InsuranceType

""" RiskProfile is a class that should hold the data, 
    basically is a centralized object that holds a 
    dictionary for access from any where in the system
"""
class RiskProfile:
    

    def get_risk_profile_map(self):
        return {
            InsuranceType.AUTO : None,
            InsuranceType.DISABILITY : None,
            InsuranceType.HOME : None,
            InsuranceType.LIFE : None
        }

    def get_base_score_map(self, questions : list) -> dict:
        if(len(questions) == 0):
            raise Exception('Risk questions must be answered')
            
        base_score_question_sum = sum(questions)

        risk_profile_score = {
            InsuranceType.AUTO : base_score_question_sum,
            InsuranceType.DISABILITY : base_score_question_sum,
            InsuranceType.HOME : base_score_question_sum,
            InsuranceType.LIFE : base_score_question_sum
        }

        return risk_profile_score