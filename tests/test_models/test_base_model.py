#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestMyBase(unittest.TestCase):

    def setUp(self):
        """Setting up instances"""
        self.base = BaseModel()
        self._new = BaseModel()

    def tearDown(self):
        """Cleaning up"""
        del self.base
        del self._new

    def test_is_created(self):
        """Testing if the instance was created"""
        self.assertTrue(self.base)
        self.assertTrue(self._new)

    def test_is_str(self):
        """Testing if attributes are strings"""
        self.assertEqual(type(self.base.id), str)

    def test_datetime_type(self):
        """Testing for datetime object"""
        self.assertEqual(type(self.base.created_at), datetime)
        self.assertEqual(type(self.base.updated_at), datetime)

    def test_class_inst(self):
        """Test if the instance is of BaseModel class"""
        self.assertEqual(type(self.base), BaseModel)

    def test_is_instance(self):
        """Test for BaseModel class"""
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_is_dict(self):
        """Test for dictionary"""
        dicty = self.base.to_dict()
        self.assertEqual(type(dicty), dict)

    def test_is_updated(self):
        """Testing if value of datetime is updated"""
        old = self.base.created_at
        self.base.save()
        self.assertIsNot(old, self._new)

    def test_is_id_diff(self):
        """Testing if instances created are different"""
        self.assertIsNot(self.base.id, self._new.id)

if __name__ == '__main__':
    unittest.main()
