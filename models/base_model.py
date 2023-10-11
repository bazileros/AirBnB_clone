import uuid
from datetime import datetime
import models
from models import Storage



class BaseModel:
    """
    Represents a base model with common attributes and methods.

    Args:
        self (BaseModel): The current instance.
    """

    def __init__(self, *extra_args, **extra_kwargs):
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
      
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        default_datetime_value = datetime.today()

        iso_format = "%Y-%m-%dT%H:%M:%S.%f"
        for key, value in extra_kwargs.items():
            if key in ["created_at", "update_at"]:
                try:
                    setattr(self, key, datetime.strptime(value, iso_format))
                except ValueError:
                    # Handle the invalid datetime format gracefully (e.g., log an error or assign a default value).
                    print(f"Warning: Invalid datetime format for key '{key}' - Using a default value.")
                    # Assign a default datetime value or take appropriate action.
                    setattr(self, key, default_datetime_value)
            else:
                setattr(self, key, value)

        if not extra_kwargs:
            models.storage.new(self)



        def save(self):
            try:
                self.updated_at = datetime.today()
                models.storage.save()
            except Exception as e:
                print(f"An error occurred while saving: {e}")


        def to_dict(self):
            result = {
                "_class": self.__class.__name_,
                "id": self.id,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat(),
            }
            result.update(self.__dict__)  # Add instance attributes
            return result
        

        def __str__(self):
            return f"[{self.__class__.__name}] ({self.id}) {self.__dict}"

