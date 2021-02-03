class MissingParamError:
    def __init__(self, StatusMessage, StatusCode):
        self.StatusCode = StatusCode
        self.StatusMessage = {'err':f'{StatusMessage} is required'}


class BadRequestError:
    def __init__(self, StatusMessage, StatusCode):
        self.StatusCode = StatusCode
        self.StatusMessage = StatusMessage


class Ok:
    def __init__(self, StatusMessage, StatusCode):
        self.StatusCode = StatusCode
        self.StatusMessage = StatusMessage
