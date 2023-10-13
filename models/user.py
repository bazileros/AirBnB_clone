#!/usr/bin/python3
"""
        Module for user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class that represents a user

    Args:
        BaseModel (email, password, first_name, last_name): empty string
    """


    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
