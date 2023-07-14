#!/usr/bin/python3
"""Create class file storage"""

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
        """Serialize __objects to the JSON file __file_path."""
        if self.__file_path is None:
            return

        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

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
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_dict = {
                        "BaseModel": BaseModel,
                        "User": User,
                        "Place": Place,
                        "State": State,
                        "City": City,
                        "Amenity": Amenity,
                        "Review": Review
                    }
                    if class_name in class_dict:
                        self.__objects[key] = class_dict[class_name](**value)
        except FileNotFoundError:
            pass

    def reload(self):
        """
        Reloads the content of the JSON file into the dictionary of objects.
        """
        if os.path.exists(self.__file_path):
            self.load()

    def __str__(self):
        """
        Returns a string representation of the FileStorage object.
        """
        return str(self.__objects)
