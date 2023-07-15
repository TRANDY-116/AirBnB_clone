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
    def __init__(self, id, created_at, updated_at):
        """
            Initialisation of public instance attributes
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at #We were asked to assign this with the current datetime. SO in that regards, it I think self.updated_at should be equal to datetime.now()
        #self.updated_at = datetime.now() #This is what I mean


    def __str__(self):
        """
            Return string representation of BaseModel class
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

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
        #Added the other attributes of this instance.
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat("%Y-%m-%dT%H:%M:%S.%f")
        obj_dict["updated_at"] = obj_dict["uodated_at"].isoformat("%Y-%m-%dT%H:%M:%S.%f")
