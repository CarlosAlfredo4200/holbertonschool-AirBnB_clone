#!/usr/bin/python3
from models.base_model import BaseModel

class Review(BaseModel):
    """Review class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Constructor for Review"""
        super().__init__(*args, **kwargs)
        