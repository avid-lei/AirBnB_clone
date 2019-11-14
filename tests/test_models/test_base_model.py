#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestMyBase(unittest.TestCase):

    def setUp(self):
        """Setting up instances"""
        self.base = BaseModel()

    def tearDown(self):
        """Cleaning up"""
        del self.base

    def test_attributes(self):
        """Testing that attributes are set"""
        self.base.name = "Diva"
        self.base.num = 20
        self.assertEqual(self.base.name, "Diva")
        self.assertEqual(self.base.num, 20)    

    def test_is_created(self):
        """Testing if the instance was created"""
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertTrue(self.base)

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
        self.assertIsInstance(self.base, BaseModel)

    def test_is_instance(self):
        """Test for BaseModel class"""
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_is_dict(self):
        """Test for dictionary"""
        self.base.num = 20
        dicty = self.base.to_dict()
        self.assertEqual(type(dicty), dict)
        self.assertIsInstance(dicty['id'], str)
        self.assertIsInstance(dicty['created_at'], str)
        self.assertIsInstance(dicty['updated_at'], str)
        self.assertIsInstance(dicty['__class__'], str)
        self.assertIsInstance(dicty['num'], int)


    def test_is_updated(self):
        """Testing if value of datetime is updated"""
        old = self.base.created_at
        self.base.save()
        new = BaseModel()
        self.assertIsNot(old, new)

    def test_is_id_diff(self):
        """Testing if instances created are different"""
        new = BaseModel()
        self.assertIsNot(self.base.id, new.id)
    
    def test_passing_int(self):
        """Testing what happens if numbers are passed into parameter"""
        new = BaseModel(5)
        self.assertIsInstance(new, BaseModel)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.id, str)
    
    def test_passing_float(self):
        new = BaseModel(6.1)
        self.assertIsInstance(new, BaseModel)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.id, str)
    
    def test_passing_list(self):
        new = BaseModel([1, 2, 3])
        self.assertIsInstance(new, BaseModel)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.id, str)

    def test_passing_string(self):
        new = BaseModel("Hello")
        self.assertIsInstance(new, BaseModel)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.id, str)
    
    def test_passing_dict(self):
        new = BaseModel({})
        self.assertIsInstance(new, BaseModel)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.id, str)
    

        

       


if __name__ == '__main__':
    unittest.main()
