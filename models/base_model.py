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
        self.updated_at = self.created_at 


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
            Returns a dictionary containing all values of __dict__
        """
        obj_dict = self.__dict__.copy()
        
