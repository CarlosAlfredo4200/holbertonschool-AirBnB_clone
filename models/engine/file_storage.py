#!/usr/bin/python3

import os
import json


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
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary of stored objects.

        Args:
            obj: Object to be stored.
        """
        obj_class_name = obj.__class__.__name__
        key = f"{obj_class_name}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Saves the dictionary of objects to a JSON file.
        """
        data = {key: obj.__dict__ for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(data, file)

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
        Creates an instance of a class based on the provided
        key and attribute values.

        Args:
            key: Key representing the class name and object ID.
            value: Dictionary of attribute values for the object.

        Returns:
            An instance of the class with the provided attribute values.
        """
        class_name, obj_id = key.split('.')
        class_ = getattr(models, class_name)
        return class_(**value)
