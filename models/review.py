#!/usr/bin/python3
"""
class review:

"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.

    Attributes:
        place_id (str): ID of the place associated with the review.
        user_id (str): ID of the user who created the review.
        text (str): Text content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
