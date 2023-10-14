#!usr/bin/python3
"""Definition of the BaseModel class."""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Serializes instances to a JSON file \
        and deserializes JSON file to instances.

        Args:
            __file_path (str): string - path to the JSON file
            __objects (dict): empty but will store \
                all objects by <class name>.id
    """

    # private instance attributes
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    # public instance methods
    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF8") as jfile:
            json.dump(json_dict, jfile)

    def reload(self):
        try:
            with open(self.__file_path, mode="r", encoding="UTF8") as file:
                jdata = json.load(file)
                for value in jdata.values():
                    myModel = value["__class__"]
                    myModel = eval(myModel)
                    obj = myModel(**value)
                    self.new(obj)
        except Exception:
            pass
