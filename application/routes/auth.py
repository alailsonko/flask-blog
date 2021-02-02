from flask import request


def auth_routes(app):

    @app.route('/signup', methods=['POST'])
    def signup():
        print(request.json['message'])

        return (request.json, 404)

    return app
