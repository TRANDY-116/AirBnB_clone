#!/usr/bin/python3
"""
    This module defines the Basemodel class
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
        Base class for other classes to inherit from
    """
    def __init__(self, *args, **kwargs):
        """
            Initialisation of public instance attributes
        """
        if kwargs is not None and kwargs != {}:
            """
                This checks if kwargs is not None
                and if Kwargs is not an empty dictionary
            """
            for keys in kwargs:
                if keys == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif keys == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[keys] = kwargs[keys]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            self.updated_at = datetime.now()

    def __str__(self):
        """
            Return string representation of BaseModel class
        """
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
            Updates updated_at attribute with current time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            Returns a dictionary containing all keys/values of __dict__
        """
        obj_dict = self.__dict__.copy()
        # Added the other attributes of this instance.
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["uodated_at"].isoformat()
