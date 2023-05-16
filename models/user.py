#!/usr/bin/python3
"""model for the class User"""
from  models.base_model import BaseModel


class User(BaseModel):
    """class for creating a user
    the information for the user are:
    email, password, first_name and last_name
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''
