#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestMyBase(unittest.TestCase):

    def setUp(self):
        self.base = BaseModel()
        self.new = BaseModel()

    def tearDown(self):
        del self.base
        del self.new

    def test_is_created(self):
        self.assertTrue(self.base)
        self.assertTrue(self.new)

    def test_is_str(self):
        self.assertEqual(type(self.base.id), str)
        self.assertEqual(type(self.base.created_at), str)
        self.assertEqual(type(self.base.updated_at), str)

    def test_class_inst(self):
        self.assertEqual(type(self.base), BaseModel)

    def test_is_instance(self):
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_is_dict(self):
        pass


    def test_is_saved(self): # ?
        pass

    def test_is_id_diff(self):
        self.assertIsNot(self.base.id, self.new.id)






    

if __name__ == '__main__':
    unittest.main()
