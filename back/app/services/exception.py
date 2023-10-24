# Exception raised when a resource is not found in the database.
class ResourceNotFound(Exception):
    """
    Exception thrown when a specific resource is not found in the database.
    """
    def __init__(self, message: str):
        """
        Initializes the exception with a provided message.
        
        Args:
        - message (str): Description of the error or the missing resource.
        """
        super().__init__(message)
