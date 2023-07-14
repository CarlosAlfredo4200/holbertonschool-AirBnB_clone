#!/usr/bin/python3
"""
class place:

"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that inherits from BaseModel.

    Attributes:
        city_id (str): ID of the city where the place is located.
        user_id (str): ID of the user who owns the place.
        name (str): Name of the place.
        description (str): Description of the place.
        number_rooms (int): Number of rooms in the place.
        number_bathrooms (int): Number of bathrooms in the place.
        max_guest (int): Maximum number of guests allowed in the place.
        price_by_night (int): Price per night for the place.
        latitude (float): Latitude coordinate of the place's location.
        longitude (float): Longitude coordinate of the place's location.
        amenity_ids (list): List of IDs of amenities associated with the place.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
