#!/usr/bin/python3
"""base model class"""
import uuid
from datetime import datetime


class BaseModel:
    """base class"""
    def __init__(self, *args, **kwargs):
        """constructor class for basemodel"""
        date_fmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, date_fmt)
                else:
                    self.__dict__[key] = val

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


