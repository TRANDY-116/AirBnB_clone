#!/usr/bin/python3
import uuid
from datetime import datetime
"""
    This module defines the Basemodel Class that defines all common attributes for other classes
"""

class Basemodel:
        """
            Base Class for Other classes to be used for the duration.
        """
        def __init__(self, *args, **kwargs):
            """
                Initialize public instance attributes
            """
            if (len(kwargs) == 0):
                self.id = str(uuid.uuid4())
                self.created_at == datetime.now()
                self.updated_at == datetime.now()
            else:
                kwargs["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                
                kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

                for key, val in kwargs.items():
                    if "__class__" not in key:
                        setattr(self, key, val)

        def __str__(self):
            """
                Return string representation of Basemodel class
            """
            return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.id, self.__dict__))





