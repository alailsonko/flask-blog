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


class BadRequestError:
    def __init__(self, StatusMessage, StatusCode):
        self.StatusCode = StatusCode
        self.StatusMessage = StatusMessage


class SignUpController:
    def __init__(self, req, EmailValidator):
        self.username = req.username
        self.email = req.email
        self.password = req.password
        self.passwordConfirm = req.passwordConfirm
        self.EmailValidator = EmailValidator

    def handle(self):
        fields = [{'key':self.username,'value': 'username'},
                  {'key':self.email,'value': 'email'},
                  {'key':self.password,'value': 'password'},
                  {'key':self.passwordConfirm,'value': 'passwordConfirm'}]
        for field in fields:
            if field['key'] == '' or field['key'] is None:
                value = field['value']
                return MissingParamError(value, 400)
        if self.password != self.passwordConfirm:
            return BadRequestError(
                'password and password confirmation must match',
                401
            )

        isEmail = self.EmailValidator(self.email)

        if isEmail.isValid() is False:
            return BadRequestError(
                'email must be a valid email',
                401
            )
