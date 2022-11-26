class InvalidPattern(Exception):
    """Raised when a string does not match a pattern"""
    def __init__(self,message: str):
        super().__init__(message)

class FileNotExists(Exception):
    """Raised when a file does not exist"""
    def __init__(self,message: str):
        super().__init__(message)

class IllegalArgument(Exception):
    """Raised when an invalid argument is provided to the program"""
    def __init__(self,message: str):
        super().__init__(message)

class ArgumentsNumber(Exception):
    """Raised when the length of the arguments is not valid"""
    def __init__(self,message: str):
        super().__init__(message)