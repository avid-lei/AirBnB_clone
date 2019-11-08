#!/usr/bin/python3
"""class Base Model"""
import uuid
from datetime import datetime


class BaseModel:
    """ class Base Model"""
    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            self.id = uuid.uuid4()
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            self.kwset(**kwargs)
    
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

    def kwset(self, **kwargs):
        for key, val in kwargs.items():
            if not key == '__class__':
                setattr(self, key, val)
        self.created_at = datetime.strptime(self.created_at,'%Y-%m-%dT%H:%M:%S.%f')
        self.updated_at = datetime.strptime(self.updated_at,'%Y-%m-%dT%H:%M:%S.%f')  
