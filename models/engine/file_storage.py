#!/usr/bin/python3

import os
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        obj_class_name = obj.__class__.__name__
        key = f"{obj_class_name}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        data = {key: obj.__dict__ for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(data, file)

    def load(self):
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                self.__objects = {key: self.__create_instance(
                    key, value) for key, value in data.items()}
        except FileNotFoundError:
            pass

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                try:
                    data = json.load(file)
                    self.__objects = {key: self.__create_instance(
                        key, value) for key, value in data.items()}
                except json.JSONDecodeError:
                    pass

    def __create_instance(self, key, value):
        class_name, obj_id = key.split('.')
        class_ = getattr(models, class_name)
        return class_(**value)
