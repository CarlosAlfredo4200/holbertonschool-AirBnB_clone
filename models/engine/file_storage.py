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

    def all(self, cls=None):
        """
        Returns a dictionary of all objects of a specific class
        or all objects if no class is specified.
        """
        if cls is None:
            return self.__objects
        else:
            obj_dict = {}
            for key, obj in self.__objects.items():
                if isinstance(obj, cls):
                    obj_dict[key] = obj
            return obj_dict

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        newObjName = obj.__class__.__name__
        self.__objects["{}.{}".format(newObjName, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Reloads the content of the JSON file into the dictionary of objects.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                try:
                    data = json.load(file)
                    for key, value in data.items():
                        class_name = value["__class__"]
                        if class_name == "BaseModel":
                            obj = BaseModel(**value)
                        elif class_name == "User":
                            obj = User(**value)
                        elif class_name == "Place":
                            obj = Place(**value)
                        elif class_name == "State":
                            obj = State(**value)
                        elif class_name == "City":
                            obj = City(**value)
                        elif class_name == "Amenity":
                            obj = Amenity(**value)
                        elif class_name == "Review":
                            obj = Review(**value)
                        else:
                            continue
                        key = "{}.{}".format(class_name, obj.id)
                        self.__objects[key] = obj
                except json.JSONDecodeError:
                    pass
