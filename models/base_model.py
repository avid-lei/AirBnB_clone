#!/usr/bin/python3
"""class Base Model"""
from models import storage
import uuid
from datetime import datetime


class BaseModel:
    """ class Base Model"""
    def __init__(self, *args, **kwargs):
        """ initialize Base Model """
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            self.kwset(**kwargs)

    def __str__(self):
        """string representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """save method"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """to dictionary method"""
        d = self.__dict__.copy()
        d['__class__'] = self.__class__.__name__
        d['updated_at'] = d['updated_at'].isoformat()
        d['created_at'] = d['created_at'].isoformat()
        return d

    def kwset(self, **kwargs):
        """set attribute from kwargs"""
        for key, val in kwargs.items():
            if not key == '__class__':
                setattr(self, key, val)
        self.created_at = datetime.strptime(self.created_at,
                                            '%Y-%m-%dT%H:%M:%S.%f')
        self.updated_at = datetime.strptime(self.updated_at,
                                            '%Y-%m-%dT%H:%M:%S.%f')
