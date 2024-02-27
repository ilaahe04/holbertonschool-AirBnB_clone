#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        with open(FileStorage.__file_path, "w") as f:
            new_dict = {}
            for k in FileStorage.__objects.keys():
                new_dict[k] = FileStorage.__objects[k].to_dict()
            string = json.dumps(new_dict)
            f.write(string)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                string = f.read()
                objs = json.loads(string)
                for i in objs.keys():
                    FileStorage.__objects[i] = BaseModel(**objs[i])
        except FileNotFoundError:
            pass
