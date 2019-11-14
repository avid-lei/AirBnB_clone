#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel
import os

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

    def has_attr(self):
        """Test that instance has all attributes"""
        self.assertTrue(hasattr(self.base, "id"))
        self.assertTrue(hasattr(self.base, "create_at"))
        self.assertTrue(hasattr(self.base, "updated_at"))
        new = BaseModel()
        new.name = "Diva"
        new.number = 5
        self.assertTrue(hasattr(new, "name"))
        self.assertTrue(hasattr(new, "number"))

        dicty = new.to_dict()

        self.assertTrue('name' in dicty)
        self.assertTrue('number' in dicty)
    

    def test_is_created(self):
        """Testing if the instance was created"""
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertTrue(self.base)

    def test_str(self):
        """Testing if attributes are strings"""
        self.assertEqual(type(self.base.id), str)
        new = BaseModel()
        strrep = "[{}] ({}) {}".format(new.__class__.__name__,
                                     new.id, new.__dict__)
        self.assertEqual(new.__str__(), strrep)
    
    def test_updated(self):
        """Test time is updated"""
        old = self.base.updated_at
        cre = self.base.created_at
        self.assertEqual(old, self.base.updated_at)
        self.assertEqual(cre, self.base.created_at)
        self.base.save()
        self.assertNotEqual(old, self.base.updated_at)
        self.assertEqual(cre, self.base.created_at)

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

    def test_diff_instance(self):
        """Test many instances"""
        new1 = BaseModel()
        new2 = BaseModel()
        new3 = BaseModel()
        new4 = BaseModel()

        self.assertIsInstance(new1.id, str)
        self.assertIsInstance(new1.updated_at, datetime)
        self.assertIsInstance(new1.created_at, datetime)

        self.assertIsInstance(new2.id, str)
        self.assertIsInstance(new2.updated_at, datetime)
        self.assertIsInstance(new2.created_at, datetime)

        self.assertIsInstance(new3.id, str)
        self.assertIsInstance(new3.updated_at, datetime)
        self.assertIsInstance(new3.created_at, datetime)

        self.assertIsInstance(new4.id, str)
        self.assertIsInstance(new4.updated_at, datetime)
        self.assertIsInstance(new4.created_at, datetime)


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
        """Testing what happens if ints are passed into parameter"""
        new = BaseModel(5)
        self.assertIsInstance(new, BaseModel)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.id, str)
    
    def test_passing_float(self):
        """Testing what happens if floats are passed into parameter"""
        new = BaseModel(6.1)
        self.assertIsInstance(new, BaseModel)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.id, str)
    
    def test_passing_list(self):
        """Testing what happens if lists are passed into parameter"""
        new = BaseModel([1, 2, 3])
        self.assertIsInstance(new, BaseModel)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.id, str)

    def test_passing_string(self):
        """Testing what happens if strings are passed into parameter"""
        new = BaseModel("Hello")
        self.assertIsInstance(new, BaseModel)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.id, str)
    
    def test_passing_dict(self):
        """Testing what happens if dicts are passed into parameter"""
        new = BaseModel({})
        self.assertIsInstance(new, BaseModel)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.id, str)

    def test_save(self):
        """Testing save and json file"""
        new = BaseModel()
        new.name = 'Diva'
        idn = '{}.{}'.format(new.__class__.__name__,
                                      new.id)
        new.save()
        with open("file.json", "r") as f:
            fc = f.read()
            self.assertTrue(idn in fc)
            self.assertTrue('name": "Diva"' in fc)
            self.assertTrue('updated_at' in fc)
            self.assertTrue('created_at' in fc)
        
        os.remove("file.json")


    



if __name__ == '__main__':
    unittest.main()
