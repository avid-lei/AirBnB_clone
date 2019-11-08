#!/usr/bin/python3
"""class Base Model"""
import uuid
import datetime


class BaseModel:
    """ lass Base Model"""

    def __init__(self):
        self.id = str(uuid.uuid4())
      
    @property
    def created_at(self):
        return self.created_at  

    @created_at.setter
    def created_at(self):
       self.created_at = datetime.isoformat(datetime.datetime.now())

    @property
    def updated_at(self):
        return self.updated_at

    @updated_at.setter
    def updated_at(self):
        self.updated_at = datetime.isoformat(datetime.datetime.now())

    def __str__(self):
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)
    



