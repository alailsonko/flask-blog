def auth_routes(app):

    @app.route('/signup', methods=['POST'])
    def signup():
        return {'message': 'working'}

    return app
