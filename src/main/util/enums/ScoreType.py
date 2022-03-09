from enum import Enum

""" Enum for ScoreType """
class ScoreType(str, Enum):
    INELIGIBLE = "ineligible",
    REGULAR = "regular",
    ECONOMIC = "economic",
    RESPONSIBLE = "responsible",

