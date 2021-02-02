class AddAccount:
    def __init__(self, username, email, password, passwordConfirm):
        self.username = username
        self.email = email
        self.password = password
        self.passwordConfirm = passwordConfirm


class MissingParamError:
    def __init__(self, StatusMessage, StatusCode):
        self.StatusCode = StatusCode
        self.StatusMessage = f'{StatusMessage} is required'


class SignUpController:
    def __init__(self, req):
        self.username = req.username
        self.email = req.email
        self.password = req.password
        self.passwordConfirm = req.passwordConfirm

    def handle(self):
        fields = [{'key':self.username,'value': 'username'},
                  {'key':self.email,'value': 'email'},
                  {'key':self.password,'value': 'password'},
                  {'key':self.passwordConfirm,'value': 'passwordConfirm'}]
        for field in fields:
            if field['key'] == '' or field['key'] is None:
                value = field['value']
                return MissingParamError(value, 400)
