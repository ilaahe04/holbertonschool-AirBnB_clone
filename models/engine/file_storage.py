#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __cls = {"BaseModel": BaseModel, "User": User, "Review": Review,
             "State": State, "City": City, "Amenity": Amenity, "Place": Place}
    __objects = {}

    @property
    def file_path(self):
        return self.__file_path

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, value):
        FileStorage.__objects = value

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
                    cn = i.split(".")[0]
                    FileStorage.__objects[i] = FileStorage.__cls[cn](**objs[i])
        except FileNotFoundError:
            pass
