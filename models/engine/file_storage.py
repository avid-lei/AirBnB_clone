#!/usr/bin/python3

import json

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        with open(self.__file_path, 'w+') as filie:
            json.dump(self.__objects.__dict__, filie)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as filie:
                self.__objects = json.load(filie)
        except FileNotFoundError:
            print("YO! FILE WAS NOT FOUND!")


