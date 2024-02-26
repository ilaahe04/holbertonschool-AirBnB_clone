#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        cn = self.__class__.__name__
        return f"[{cn}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = {}
        new_dict["__class__"] = self.__class__.__name__
        for k in self.__dict__.keys():
            if k == "created_at" or k == "updated_at":
                t = self.__dict__[k].isoformat()
                new_dict[k] = self.__dict__[k]
            else:
                new_dict[k] = self.__dict__[k]
        return new_dict
