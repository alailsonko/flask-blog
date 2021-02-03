from application.cryptograph.password_hash import PasswordHasher
from application.usecases.add_account import AddAccount
from application.validators.email_validator import EmailValidator
from application.controllers.signup_controller import SignUpController
from application.models import User, db


class FactorySignUpController:
    def __init__(self, data):
        self.data = data

    def handle(self):
        username = self.data['username'] or ''
        email = self.data['email'] or ''
        password = self.data['password'] or ''
        passwordConfirm = self.data['passwordConfirm'] or ''

        req = AddAccount(username, email, password, passwordConfirm)
        database = db
        makeSignUpController = SignUpController(
            req,
            EmailValidator,
            PasswordHasher,
            database,
            User
        )

        return makeSignUpController.handle()
