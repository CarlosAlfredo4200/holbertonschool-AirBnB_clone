#!/usr/bin/python3
"""
class base_model

"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class that serves as the base model for other classes.

    Attributes:
        id (str): Unique identifier for the model instance.
        created_at (datetime): Datetime when the model instance was created.
        updated_at (datetime): Datetime when the model instance was last updated.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes a new BaseModel instance.

        Args:
            args: Variable length argument list.
            kwargs: Arbitrary keyword arguments.
        """
        from models import storage

        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: String representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """
        Updates the updated_at attribute and saves the BaseModel instance.
        """
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """
        Converts the BaseModel instance to a dictionary representation.

        Returns:
            dict: Dictionary representation of the BaseModel instance.
        """
