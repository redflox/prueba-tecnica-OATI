
# Exepcion cuando no se encuentra un recurso en la db
class ResourceNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)