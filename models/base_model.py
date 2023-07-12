#!/usr/bin/python3
"""a class BaseModel"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Constructor for BaseModel.

        Args:
            *args: Variable-length arguments.

        If kwargs is not empty:
            - Each key of the dictionary
            is an attribute name (excluding '__class__').
            - Each value of the dictionary is the value
            for the corresponding attribute name.

        If kwargs is empty:
            - The 'id' attribute is assigned a unique identifier.
            - The 'created_at' attribute is set to the current datetime.
            - The 'updated_at' attribute is set to the current datetime.

        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def __str__(self):
        """
        Return a string representation of the BaseModel object.

        Returns:
            str: A string representation in the format:
                 "[<class name>] (<id>) <attribute dictionary>"
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the 'updated_at' attribute with the current datetime.

        """
        self.updated_at = datetime.today()
        from models import storage
        storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel object.

        Returns:
            dict: A dictionary containing all keys/values
            of the instance's __dict__,
            including '__class__', 'created_at', and 'updated_at'.
            The 'created_at'
            and 'updated_at' values are converted
            to string objects in ISO format.

        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
