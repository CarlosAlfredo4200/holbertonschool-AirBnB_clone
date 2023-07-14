#!/usr/bin/python3
"""Create class file storage"""

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    FileStorage class that manages the storage
    and retrieval of objects in a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of stored objects.
        """
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        newObjName = obj.__class__.__name__
        self.__objects["{}.{}".format(newObjName, obj.id)] = obj

    def save(self):
        """
        This method saves the dictionary of objects to the JSON file.
        """
        objects_dict = {}
        for key, value in self.__objects.items():
            objects_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as fl:
            json.dump(objects_dict, fl, indent=4)

    def load(self):
        """
        Loads the content of the JSON file into the dictionary of objects.
        If the file doesn't exist, no exception is raised.
        """
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                self.__objects = {key: self.__create_instance(
                    key, value) for key, value in data.items()}
        except FileNotFoundError:
            pass

    def reload(self):
        """
        Reloads the content of the JSON file into the dictionary of objects.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                try:
                    data = json.load(file)
                    self.__objects = {key: self.__create_instance(
                        key, value) for key, value in data.items()}
                except json.JSONDecodeError:
                    pass

    def __create_instance(self, key, value):
        """
        Creates an instance of a class based on the key and value.

        Args:
            key (str): Key representing the class name and object id.
            value (dict): Dictionary containing the attributes of the object.

        Returns:
            instance: An instance of the class represented by the key.

        """
        class_name, obj_id = key.split('.')
        class_dict = {"BaseModel": BaseModel, "User": User}
        if class_name in class_dict:
            return class_dict[class_name](**value)
        else:
            return None

    def __create_instance(self, key, value):
        """
        Creates an instance of a class based on the key and value.

        Args:
            key (str): Key representing the class name and object id.
            value (dict): Dictionary containing the attributes of the object.

        Returns:
            instance: An instance of the class represented by the key.

        """
        class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }
        class_name, obj_id = key.split('.')
        if class_name in class_dict:
            return class_dict[class_name](**value)
        else:
            return None
