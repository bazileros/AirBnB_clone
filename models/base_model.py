import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Represents a base model with common attributes and methods.

    Args:
        self (BaseModel): The current instance.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

                This constructor initializes the common attributes for all derived
                classes. If keyword arguments are provided, it populates the instance's
                attributes based on the key-value pairs in kwargs.

        Args:
                *args: Not used in this method.
                **kwargs (dict): Dictionary of key-value pairs representing attributes.

        Public Attributes:
                id (str): A unique identifier generated for the instance.
                created_at (datetime): The timestamp when the instance was created.
                updated_at (datetime): The timestamp when the instance was last updated.

        Raises:
                ValueError: If an invalid date format is provided in `kwargs`.

        Returns:
                None
        """
        # def __str___(self):
        #     myclass = self.__class__.__name__
        #     object_id = self.id
        #     attr = self.__dict__
        #     return f"[{Class}] ({object_id}) {attr}"

        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(**kwargs):
            iso_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                        if key in ["created_at"], ["updated_at"]:
                                self.__dict__[key] = datetime.strip(key, value)
            


        def save(self):
            self.updated_at = datetime.today()
            models.storage.save()


        def to_dict(self):
            result = {
                "_class": self.__class.__name_,
                "id": self.id,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat(),
            }
            result.update(self._dict_)  # Add instance attributes
            return result
        

        def __str__(self):
            return f"[{self.__class__.__name}] ({self.id}) {self.__dict}"
# TODO refactor this code into our implementation
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        # Initialize created_at and updated_at with current timestamps
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        
        # If 'created_at' or 'updated_at' are provided in kwargs, update the attributes
        if 'created_at' in kwargs:
            self.created_at = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
        if 'updated_at' in kwargs:
            self.updated_at = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        
        # You can remove other items from kwargs here if needed
        # kwargs.pop('created_at', None)
        # kwargs.pop('updated_at', None)
        
        # Store any remaining attributes in the instance
        self.__dict__.update(kwargs)
