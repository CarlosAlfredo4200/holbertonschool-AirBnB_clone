#!/usr/bin/python3
"""
calss Module Name:

"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from os import path


class FileStorage:
    """
    FileStorage class that manages the storage and retrieval of objects in a JSON file.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary of stored objects.
    """

    def __init__(self):
        """
        Initializes a new FileStorage instance.
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        Returns the dictionary of stored objects.

        Returns:
            dict: Dictionary of stored objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary of stored objects.

        Args:
            obj: Object to be added to the dictionary.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the objects to the JSON file.
        """
        objects_dict = {}
