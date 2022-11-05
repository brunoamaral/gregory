
# Exceptions needed to validate API authorization

class APIError(Exception):
     def __init__(self, message):
        super().__init__(message)


class APINoAPIKeyError(APIError):
     def __init__(self, message):
        super().__init__(message)


class APIInvalidAPIKeyError(APIError):
     def __init__(self, message):
        super().__init__(message)


class APIInvalidIPAddressError(APIError):
     def __init__(self, message):
        super().__init__(message)


class APIAccessDeniedError(APIError):
     def __init__(self, message):
        super().__init__(message)
