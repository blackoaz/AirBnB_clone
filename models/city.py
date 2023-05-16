#!/usr/bin/python3
"""model class for city"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class inheriting from base model"""
    state_id = ''
    name = ''
