#!/usr/bin/python3
"""
    user module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        User class for all other classes
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
            initializes the instance of an object
        """
        super().__init__(*args, **kwargs)
