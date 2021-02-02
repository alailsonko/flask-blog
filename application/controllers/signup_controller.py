class AddAccount:
    def __init__(self, username, email, password, passwordConfirm):
        self.username = username
        self.email = email
        self.password = password
        self.passwordConfirm = passwordConfirm


class MissingParamError:
    def __init__(self, StatusMessage, StatusCode):
        self.StatusCode = StatusCode
        self.StatusMessage = StatusMessage


class SignUpController:
    def __init__(self, req):
        self.username = req.username
        self.email = req.email
        self.password = req.password
        self.passwordConfirm = req.passwordConfirm

    def handle(self):
        if self.username == '' or self.username is None:
            return MissingParamError('username is required', 400)
        if self.email == '' or self.email is None:
            return MissingParamError('email is required', 400)
        if self.password == '' or self.password is None:
            return MissingParamError('password is required', 400)
        if self.passwordConfirm == '' or self.passwordConfirm is None:
            return MissingParamError('passwordConfirm is required', 400)
