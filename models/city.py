
#!/usr/bin/python3
"""This is the City Model module.

Contains the City class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
        """
            This class defines a City
        """
        
        state_id = ""
        name = ""
