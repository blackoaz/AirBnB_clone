#!/usr/bin/python3
"""base model class"""
import uuid
from datetime import datetime


class BaseModel:
    """base class"""
    def __init__(self):
        """constructor class for basemodel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """Method for creating a dictionary for th class"""
        data_dict = self.__dict__.copy()
        data_dict["__class__"] = self.__class__.__name__
        data_dict["created_at"] = self.created_at.isoformat()
        data_dict["updated_at"] = self.updated_at.isoformat()

        return data_dict

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)


