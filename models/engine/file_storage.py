#!/usr/bin/python3
"""file storage class"""
import json


class FileStorage:
    """class FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects['{}.{}'.format(obj.__class__.__name__,
                                      obj.id)] = obj.to_dict()

    def save(self):
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f, default=str)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except:
            pass
