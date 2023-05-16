#!/usr/bin/python3
"""model class for Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class inheriting from BaseModel"""
    place_id = ''
    user_id = ''
    text = ''
