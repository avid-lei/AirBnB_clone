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

    # check if the file doesn't exist before running (not sure tho)
    # def test_if_exists_before(self):
    #     self.assertFalse(os.path.exists("file.json"))

    # check if FileStorage has the 2 public attributes (why tho?) (hasassr?)
    def test_if_attrs_exist(self):
        self.assertTrue(hasattr(self.stor, '_FileStorage__file_path'))
        self.assertTrue(hasattr(self.stor, '_FileStorage__file_path'))

    # check is all() returns a dictionary
    def test_all(self):
        self.assertEqual(type(self.stor.all()), dict)

    # check type of every key in the dict (?)
    def test_dict_json(self):
        pass

    # pass an instance to save() and check if the file exists (after reloading)
    def test_save(self):
        self.base.save()
        self.assertTrue(os.path.exists('file.json'))

    # check if the file is not empty
    def test_empty_file(self):
        self.assertFalse(os.stat('file.json') == 0)

    # pass instance to save() again and check if file have changed the lenght
    def test_file_change(self):
        info = os.stat('file.json')
        before = info.st_size
        self.new.save()
        info = os.stat('file.json')
        after = info.st_size
        self.assertFalse(before == after)

    # check methods with too many arguments
    def test_too_many_all(self):
        with self.assertRaises(TypeError) as omg:
            self.stor.save('omg', 'lol', 'dolls')
        self.assertTrue(omg)

    def test_too_many_new(self):
        with self.assertRaises(TypeError) as omg:
            self.stor.save('omg', 'lol', 'dolls')
        self.assertTrue(omg)

    def test_too_little_new(self):
        with self.assertRaises(TypeError) as omg:
            self.stor.save('omg', 'lol', 'dolls')
        self.assertTrue(omg)

    def test_too_many_save(self):
        with self.assertRaises(TypeError) as omg:
            self.stor.save('omg', 'lol', 'dolls')
        self.assertTrue(omg)

    def test_too_many_reload(self):
        with self.assertRaises(TypeError) as omg:
            self.stor.save('omg', 'lol', 'dolls')
        self.assertTrue(omg)

if __name__ == '__main__':
    unittest.main()
