#!/usr/bin/python3
"""Test class for user model"""
import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test cases for User"""
    def test_basemodel_id(self):
        """Testing if user id is a string"""
        model = User()
        self.assertIsInstance(model.id, str)

    def test_updated_at_format(self):
        """Testing the format of updated_at"""
        model = User()
        self.assertIsInstance(model.updated_at, datetime)

    def test_created_at_format(self):
        """Testing the format of created_at"""
        model = User()
        self.assertIsInstance(model.created_at, datetime)

    def test_create_from_dict(self):
        """Testing the instances created from dictionary
        """
        kwargs = {'my_number': 89,
                  'name': 'My First Model',
                  '__class__': 'User',
                  'updated_at': '2017-09-28T21:05:54.119572',
                  'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                  'created_at': '2017-09-28T21:05:54.119427'}
        model = User(**kwargs)
        self.assertEqual(model.__class__.__name__, 'User')
        self.assertEqual(model.id, 'b6a6e15c-c67d-4312-9a75-9d084935e579')
        self.assertEqual(model.my_number, 89)

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_conformance_user(self):
        """Testing if User conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
