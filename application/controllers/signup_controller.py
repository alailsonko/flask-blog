from sqlalchemy.exc import IntegrityError
from application.helpers.http_helper import (
    MissingParamError,
    BadRequestError,
    Ok
)


class SignUpController:
    def __init__(self, req, EmailValidator, PasswordHasher, database, User):
        self.__username = req.username
        self.__email = req.email
        self.__password = req.password
        self.__passwordConfirm = req.passwordConfirm
        self.__EmailValidator = EmailValidator
        self.__PasswordHasher = PasswordHasher
        self.__database = database
        self.__User = User

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
                {'err':'password and password confirmation must match'},
                400
            )

        isEmail = self.__EmailValidator(self.__email)
        print(isEmail.isValid())
        if isEmail.isValid() is not True:
            return BadRequestError(
                {'err':'email must be a valid email'},
                400
            )

        hashed = self.__PasswordHasher(self.__password)

        if hashed.hash() == f'{self.__password}':
            return BadRequestError(
                {'err':'internal server error'},
                400
            )
        user = self.__User(username=self.__username, email=self.__email, password=hashed.hash())
        try:

            self.__database.session.add(user)
            self.__database.session.commit()
            user_created = user
            del user_created.password
            json = {
                'id': user_created.id,
                'username': user_created.username,
                'email': user_created.email,
            }
            return Ok(
                json,
                200
            )

        except IntegrityError:
            return BadRequestError(
                {'err':'email or username already exists'},
                400
            )
