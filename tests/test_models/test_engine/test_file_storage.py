#!/usr/bin/python3

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class testMyDict(unittest.TestCase):
    """Class to check FileStprage class"""

    def setUp(self):
        """Setting up instances"""
        self.base = BaseModel()
        self.new = BaseModel()
        self.stor = FileStorage()

    def tearDown(self):
        """Cleaning up"""
        del self.base
        del self.stor
        del self.new

    def test_if_private(self):
        """Check if the attribute is private"""
        mess = "'FileStorage' object has no attribute '_testMyDict__objects'"
        self.stor = FileStorage()
        with self.assertRaises(AttributeError) as err:
            print(self.stor.__objects)
        self.assertEqual(message, str(err.exception))

    def test_if_isinstance(self):
        """Check if the instances belong to the classes"""
        self.assertIsInstance(self.base, BaseModel)
        self.assertIsInstance(self.new, BaseModel)
        self.assertIsInstance(self.stor, FileStorage)

    def test_if_attrs_exist(self):
        """Check if FileStorage has the 2 public attributes"""
        self.assertTrue(hasattr(self.stor, '_FileStorage__file_path'))
        self.assertTrue(hasattr(self.stor, '_FileStorage__objects'))

    def test_all(self):
        """Check is all() returns a dictionary"""
        self.assertEqual(type(self.stor.all()), dict)

    def test_dict_json(self):
        """Check type of every val in the dict"""
        self.base.num = 20
        dicty = self.base.to_dict()
        self.assertEqual(type(dicty), dict)
        self.assertIsInstance(dicty['id'], str)
        self.assertIsInstance(dicty['created_at'], str)
        self.assertIsInstance(dicty['updated_at'], str)
        self.assertIsInstance(dicty['__class__'], str)
        self.assertIsInstance(dicty['num'], int)

    def test_save(self):
        """Check if save() creates a file"""
        self.base.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_empty_file(self):
        """Check if the file is not empty"""
        self.assertFalse(os.stat('file.json') == 0)

    def test_file_change(self):
        """Check if the file changed its size"""
        info = os.stat('file.json')
        before = info.st_size
        self.new.save()
        info = os.stat('file.json')
        after = info.st_size
        self.assertFalse(before == after)

    def test_too_many_all(self):
        """Check all() method with too many arguments"""
        with self.assertRaises(TypeError) as omg:
            self.stor.all('omg', 'lol', 'dolls')
        self.assertTrue(omg)

    def test_too_many_new(self):
        """Check new() method with too many arguments"""
        with self.assertRaises(TypeError) as omg:
            self.stor.new('omg', 'lol', 'dolls')
        self.assertTrue(omg)

    def test_too_little_new(self):
        """Check new() method with 1 argument"""
        with self.assertRaises(TypeError) as omg:
            self.stor.new()
        self.assertTrue(omg)

    def test_too_many_save(self):
        """Check save() method with too many arguments"""
        with self.assertRaises(TypeError) as omg:
            self.stor.save('omg', 'lol', 'dolls')
        self.assertTrue(omg)

    def test_too_many_reload(self):
        """Check reload() method with too many arguments"""
        with self.assertRaises(TypeError) as omg:
            self.stor.reload('omg', 'lol', 'dolls')
        self.assertTrue(omg)

if __name__ == '__main__':
    unittest.main()
