#!/usr/bin/python3
"""
class city:

"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.

    Attributes:
        state_id (str): ID of the state to which the city belongs.
        name (str): Name of the city.
    """

    state_id = ""
    name = ""
