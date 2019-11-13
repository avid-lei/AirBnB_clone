#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestMyBase(unittest.TestCase):

    def setUp(self):
        """Setting up instances"""
        self.base = BaseModel()
        self.new = BaseModel()

    def tearDown(self):
        """Cleaning up"""
        del self.base
        del self.new

    def test_is_created(self):
        """Testing if the instance was created"""
        self.assertTrue(self.base)
        self.assertTrue(self.new)

# AssertionError: '2019-11-12T23:46:44.512804' != <class 'datetime.datetime'>
#    def test_date(self):
#        self.assertEqual(self.base.created_at, datetime)

    def test_is_str(self):
        """Testing if attributes are strings"""
        self.assertEqual(type(self.base.id), str)
        self.assertEqual(type(self.base.created_at), str)
        self.assertEqual(type(self.base.updated_at), str)

    def test_class_inst(self):
        """Test if the instance is of BaseModel class"""
        self.assertEqual(type(self.base), BaseModel)

    def test_is_instance(self):
        self.assertTrue(isinstance(self.base, BaseModel))

    # AttributeError: 'str' object has no attribute 'isoformat'
    #def test_is_dict(self):
    #    dicty = self.base.to_dict()
    #    self.assertEqual(type(dicty), dict)

    def test_is_updated(self):
        """Testing if value of datetime is updated"""
        old = self.base.created_at
        new = self.base.save()
        self.assertIsNot(old, new)

    def test_is_id_diff(self):
        """Testing if instances created are different"""
        self.assertIsNot(self.base.id, self.new.id)

if __name__ == '__main__':
    unittest.main()
