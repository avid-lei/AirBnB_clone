#!/usr/bin/python3
"""class Base Model"""
import uuid
from datetime import datetime


class BaseModel:
    """ class Base Model"""
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        d = self.__dict__
        d['__class__'] = 'BaseModel'
        d['updated_at'] = self.updated_at.isoformat()
        d['created_at'] = self.created_at.isoformat()
        return d
