from enum import Enum

""" Enum for InsuranceType """
class InsuranceType(str, Enum):
    AUTO = "auto",
    DISABILITY = "disability",
    HOME = "home",
    LIFE = "life",

