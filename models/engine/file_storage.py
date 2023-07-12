#!/usr/bin/python3

import os
import json
from models.base_model import BaseModel


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
        """Serialize __objects to the JSON file __file_path."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

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
        class_dict = {"BaseModel": BaseModel}
        if class_name in class_dict:
            return class_dict[class_name](**value)
        else:
            return None
