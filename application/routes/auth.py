from flask import request
from application.factory.make_signup_controller import FactorySignUpController
from .adapter_controller import AdapterController


def auth_routes(app):

    @app.route('/signup', methods=['POST'])
    def signup():
        data = request.json
        return AdapterController(FactorySignUpController(data).handle())

    return app
