


# Base exception class
class VolarisException(Exception):
    pass


class RecorderInitializationError(VolarisException):
    """Error type for re-initialization when starting an experiment"""


class LoadObjectError(VolarisException):
    """Error type for Recorder when can not load object"""


class ExpAlreadyExistError(Exception):
    """Experiment already exists"""
