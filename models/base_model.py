#!/usr/bin/python3
'''
My BaseModel Module
'''
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    '''
    My BaseModel
    '''
    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            for k in kwargs.keys():
                if k == "created_at" or k == "updated_at":
                    t = datetime.strptime(kwargs[k], '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, k, t)
                elif k == "__class__":
                    continue
                else:
                    setattr(self, k, kwargs[k])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        cn = self.__class__.__name__
        return f"[{cn}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        new_dict = {}
        new_dict["__class__"] = self.__class__.__name__
        for k in self.__dict__.keys():
            if isinstance(self.__dict__[k], datetime):
                t = self.__dict__[k].isoformat()
                new_dict[k] = t
            else:
                new_dict[k] = self.__dict__[k]
        return new_dict
