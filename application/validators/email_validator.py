import validators


class EmailValidator:
    def __init__(self, emailValidate):
        self.emailValidate = emailValidate

    def isValid(self):
        return validators.email(self.emailValidate)
