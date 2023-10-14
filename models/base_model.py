#!/usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Represents a base model with common attributes and methods.
    """

    def __init__(self, *extra_args, **extra_kwargs):
        """Initialize the BaseModel class

        Args:
            self (BaseModel): the current instance
            extra_args (any): not used here
            extra_kwargs (dict): dictionary of key/value pair attributes

        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        default_datetime_value = datetime.today()
        iso_format = "%Y-%m-%dT%H:%M:%S.%f"

        if extra_kwargs:
            for key, value in extra_kwargs.items():
                if key == "__class__":
                    self.__class__.__name__ = value
                elif key == "created_at":
                    self.created_at = datetime.datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key == "updated_at":
                    self.updated_at = datetime.datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"
                    )
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Returns the string representation of the class.
        Returns:
            str: The string representation of the class.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Saves the instance and updates the `updated_at` attribute.
        """
        try:
            self.updated_at = datetime.today()
            models.storage.new(self)
            models.storage.save()
        except Exception as e:
            print(f"An error occurred while saving: {e}")

    # def to_dict(self):
    #     """
    #     Converts the instance to a dictionary representation.
    #     Returns:
    #         dict: A dictionary representation of the instance.
    #     """
    #     result = {
    #         "_class": self.__class__.__name__,
    #         "id": self.id,
    #         "created_at": self.created_at,
    #         "updated_at": self.updated_at,
    #     }
    #     result.update(self.__dict__)  # Add instance attributes
    #     return result
    # def to_dict(self):
    #     """Returns a dictionary containing all \
    #         keys/values of __dict__ of the instance."""
    #     dict_copy = self.__dict__.copy()
    #     dict_copy["created_at"] = self.created_at
    #     dict_copy["updated_at"] = self.updated_at
    #     dict_copy["__class__"] = self.__class__.__name__

    #     return dict_copy

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        # return {
        #     **self.__dict__,
        #     '__class__': self.__class__.__name__,

        # }
        dict_array = {}
        for key, value in self.__dict__.items():
            if key != "created_at" and key != "updated_at":
                dict_array[key] = value
        dict_array["__class__"] = self.__class__.__name__
        dict_array["created_at"] = self.created_at.isoformat()
        dict_array["updated_at"] = self.updated_at.isoformat()
        return dict_array
