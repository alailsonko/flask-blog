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
        self.__username = req.username
        self.__email = req.email
        self.__password = req.password
        self.__passwordConfirm = req.passwordConfirm
        self.__EmailValidator = EmailValidator

    def handle(self):
        fields = [{'key':self.__username,'value': 'username'},
                  {'key':self.__email,'value': 'email'},
                  {'key':self.__password,'value': 'password'},
                  {'key':self.__passwordConfirm,'value': 'passwordConfirm'}]
        for field in fields:
            if field['key'] == '' or field['key'] is None:
                value = field['value']
                return MissingParamError(value, 400)
        if self.__password != self.__passwordConfirm:
            return BadRequestError(
                'password and password confirmation must match',
                401
            )

        isEmail = self.__EmailValidator(self.__email)

        if isEmail.isValid() is False:
            return BadRequestError(
                'email must be a valid email',
                401
            )
