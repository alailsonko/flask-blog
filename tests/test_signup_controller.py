from application.controllers.signup_controller import SignUpController
from application.usecases.add_account import AddAccount
from application.models import User
import bcrypt

from pytest_mock import MockerFixture


class PasswordHasher:
    def __init__(self, password):
        self.password = password

    def hash(self):
        # hashed = bcrypt.hashpw( b'{self.password}', bcrypt.gensalt())
        return f'{self.password}'


class EmailValidator:
    def __init__(self, email):
        self.email = email

    def isValid(self):
        return False


class TestClassSignUpController:
    """
    Case username is not provided throw error
    """
    def test_username_is_required(self, database):
        username = ''
        email = 'valid_email@mail.com'
        password = 'valid_password'
        passwordConfirm = 'valid_password'
        req = AddAccount(username, email, password, passwordConfirm)
        sut = SignUpController(req, EmailValidator, PasswordHasher, database, User)
        assert sut.handle().StatusCode == 400
        assert sut.handle().StatusMessage == 'username is required'
    """
    Case email is not provided throw error
    """
    def test_email_is_required(self, database):
        username = 'valid_user'
        email = ''
        password = 'valid_password'
        passwordConfirm = 'valid_password'
        req = AddAccount(username, email, password, passwordConfirm)
        sut = SignUpController(req, EmailValidator, PasswordHasher, database, User)

        assert sut.handle().StatusCode == 400
        assert sut.handle().StatusMessage == 'email is required'

    """
    Case password is not provided throw error
    """
    def test_password_is_required(self, database):
        username = 'valid_user'
        email = 'valid_mail@mail.com'
        password = ''
        passwordConfirm = 'valid_password'
        req = AddAccount(username, email, password, passwordConfirm)
        sut = SignUpController(req, EmailValidator, PasswordHasher, database, User)

        assert sut.handle().StatusCode == 400
        assert sut.handle().StatusMessage == 'password is required'

    """
    Case password is not provided throw error
    """
    def test_passwordConfirm_is_required(self, database):
        username = 'valid_user'
        email = 'valid_mail@mail.com'
        password = 'valid_password'
        passwordConfirm = ''
        req = AddAccount(username, email, password, passwordConfirm)
        sut = SignUpController(req, EmailValidator, PasswordHasher, database, User)

        assert sut.handle().StatusCode == 400
        assert sut.handle().StatusMessage == 'passwordConfirm is required'

    def test_password_passwordConfirm_is_equal(self, database):
        username = 'valid_user'
        email = 'valid_mail@mail.com'
        password = 'valid_password'
        passwordConfirm = 'invalid_password'
        req = AddAccount(username, email, password, passwordConfirm)
        sut = SignUpController(req, EmailValidator, PasswordHasher, database, User)

        assert sut.handle().StatusCode == 401
        assert sut.handle().StatusMessage == 'password and password confirmation must match'

    def test_email_is_valid(self, database):
        username = 'valid_user'
        email = 'invalid_mail@mail.com'
        password = 'valid_password'
        passwordConfirm = 'valid_password'
        req = AddAccount(username, email, password, passwordConfirm)
        sut = SignUpController(req, EmailValidator, PasswordHasher, database, User)
        assert sut.handle().StatusCode == 401
        assert sut.handle().StatusMessage == 'email must be a valid email'

    def test_password_is_hashed(self, mocker: MockerFixture, database):
        username = 'valid_user'
        email = 'valid_mail@mail.com'
        password = 'valid_password'
        passwordConfirm = 'valid_password'
        req = AddAccount(username, email, password, passwordConfirm)

        class EmailValidatorr:
            def __init__(self, email):
                self.email = email

            def isValid(self):
                return True

        # mocker.patch('EmailValidator.isValid()', return_value=True)
        sut = SignUpController(req, EmailValidatorr, PasswordHasher, database, User)

        assert sut.handle().StatusCode == 401
        assert sut.handle().StatusMessage == 'internal server error'

    def test_user_created(self, mocker: MockerFixture, database):
        username = 'valid_user'
        email = 'valid_mai1@mail.com'
        password = 'valid_password'
        passwordConfirm = 'valid_password'
        req = AddAccount(username, email, password, passwordConfirm)

        class EmailValidatorr:
            def __init__(self, email):
                self.email = email

            def isValid(self):
                return True

        class PasswordHasherr:
            def __init__(self, password):
                self.password = password

            def hash(self):
                hashed = bcrypt.hashpw(b'{self.password}', bcrypt.gensalt())
                return hashed

        sut = SignUpController(req, EmailValidatorr, PasswordHasherr, database, User)
        # assert sut.handle().StatusCode == 200
        assert sut.handle().StatusMessage.password is None
