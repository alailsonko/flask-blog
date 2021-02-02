from application.controllers.signup_controller import AddAccount, SignUpController


class EmailValidator:
    def __init__(self, email):
        self.email = email

    def isValid(self):
        return False


class TestClassSignUpController:
    """
    Case username is not provided throw error
    """
    def test_username_is_required(self):
        username = ''
        email = 'valid_email@mail.com'
        password = 'valid_password'
        passwordConfirm = 'valid_password'
        req = AddAccount(username, email, password, passwordConfirm)
        sut = SignUpController(req, EmailValidator)

        assert sut.handle().StatusCode == 400
        assert sut.handle().StatusMessage == 'username is required'
    """
    Case email is not provided throw error
    """
    def test_email_is_required(self):
        username = 'valid_user'
        email = ''
        password = 'valid_password'
        passwordConfirm = 'valid_password'
        req = AddAccount(username, email, password, passwordConfirm)
        sut = SignUpController(req, EmailValidator)

        assert sut.handle().StatusCode == 400
        assert sut.handle().StatusMessage == 'email is required'

    """
    Case password is not provided throw error
    """
    def test_password_is_required(self):
        username = 'valid_user'
        email = 'valid_mail@mail.com'
        password = ''
        passwordConfirm = 'valid_password'
        req = AddAccount(username, email, password, passwordConfirm)
        sut = SignUpController(req, EmailValidator)

        assert sut.handle().StatusCode == 400
        assert sut.handle().StatusMessage == 'password is required'

    """
    Case password is not provided throw error
    """
    def test_passwordConfirm_is_required(self):
        username = 'valid_user'
        email = 'valid_mail@mail.com'
        password = 'valid_password'
        passwordConfirm = ''
        req = AddAccount(username, email, password, passwordConfirm)
        sut = SignUpController(req, EmailValidator)

        assert sut.handle().StatusCode == 400
        assert sut.handle().StatusMessage == 'passwordConfirm is required'

    def test_password_passwordConfirm_is_equal(self):
        username = 'valid_user'
        email = 'valid_mail@mail.com'
        password = 'valid_password'
        passwordConfirm = 'invalid_password'
        req = AddAccount(username, email, password, passwordConfirm)
        sut = SignUpController(req, EmailValidator)

        assert sut.handle().StatusCode == 401
        assert sut.handle().StatusMessage == 'password and password confirmation must match'

    def test_email_is_valid(self):
        username = 'valid_user'
        email = 'invalid_mail@mail.com'
        password = 'valid_password'
        passwordConfirm = 'valid_password'
        req = AddAccount(username, email, password, passwordConfirm)
        sut = SignUpController(req, EmailValidator)

        assert sut.handle().StatusCode == 401
        assert sut.handle().StatusMessage == 'email must be a valid email'
