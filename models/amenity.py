#!/usr/bin/python3
"""
    amenity module
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        Amenity class for all User object
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
            initializes the instance of an object
        """
        super().__init__(*args, **kwargs)
