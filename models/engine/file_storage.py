#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()

    def save(self):
        with open(FileStorage.__file_path, "w") as f:
            string = json.dumps(FileStorage.__objects)
            f.write(string)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                string = f.read()
                objs = json.loads(string)
                for i in objs.keys():
                    obj = BaseModel(**objs[i])
                    FileStorage.__objects[i] = obj.to_dict()
        except FileNotFoundError:
            pass
