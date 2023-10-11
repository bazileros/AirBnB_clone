import uuid
from datetime import datetime

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
               self.created_at = datetime.today()
               self.updated_at = datetime.today()
               self.id = str(uuid.uuid4())
               # TODO convert datetime to iso format

