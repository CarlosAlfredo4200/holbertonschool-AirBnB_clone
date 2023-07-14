#!/usr/bin/python3
"""
class user

"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel.

    Attributes:
        email (str): Email of the user.
        password (str): Password of the user.
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
    """
  
    email = ""
    password = ""
    first_name = ""
    last_name = ""
