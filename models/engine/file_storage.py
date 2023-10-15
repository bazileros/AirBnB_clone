#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import os


class FileStorage:

    """Class for serializtion and deserialization of base classes."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of objects stored in the FileStorage instance.

        This method retrieves the dictionary containing all objects currently managed by
        the FileStorage class instance. The dictionary is structured with unique keys
        corresponding to the object types and IDs.

        Args:
            self: An instance of the FileStorage class.

        Returns:
            dict: A dictionary of objects in the format {key: object}.

    """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object to the FileStorage instance.

        This method adds a new object to the list of objects managed by the FileStorage class
        instance. The object is identified by its type and ID, and it is stored in the
        `__objects` dictionary.

        Args:
            self: An instance of the FileStorage class.
            obj: The object to be added.

        Returns:
            None
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize the `__objects` dictionary to a JSON file.

        This method is responsible for saving the current state of the objects managed by the
        FileStorage class into a JSON file. It opens the specified file path, serializes the
        objects into a JSON format, and writes the data to the file.

        Args:
            self: An instance of the FileStorage class.

        Returns:
            None

        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json_dict = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
            json.dump(json_dict, f, indent=4)

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """
        Deserialize a JSON file and load its contents into the __objects dictionary.

        This method is responsible for deserializing a JSON file and loading its contents into
        the '__objects' dictionary of the FileStorage class. The JSON file is specified by the
        `__file_path` attribute of the FileStorage class.

        Args:
            self: An instance of the FileStorage class.

        Returns:
            None
        """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {key: self.classes()[value["__class__"]](**value)
                        for key, value in obj_dict.items()}

            FileStorage.__objects = obj_dict

    def attributes(self):
        """
        Retrieve the valid attributes and their types for each class in the application.

        This method returns a dictionary that specifies the valid attributes and their associated
        data types for each class used in the application. It provides a structured overview of
        the expected attributes for each class, making it a valuable reference for developers.

        Args:
            self: An instance of the class containing the 'attributes' method.

        Returns:
            dict: A dictionary containing class names as keys and a sub-dictionary as values.
                The sub-dictionary contains attribute names as keys and their corresponding data types.

        """
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
