from abc import ABC, abstractmethod

"""Abstract class Validator for creating a signature for the method validate, which can be used for different types of validations if needed"""
class Validator(ABC):
    @abstractmethod
    def validate(self , score : dict) -> dict:
        """ Method responsible for validating whatever the score is for a given validation type """