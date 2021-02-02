def initialize_app(config_name):

    from .routes.auth import auth_routes
    from .create_app.app import create_app

    app = create_app(config_name)

    routes = [auth_routes]

    for route in routes:
        app = route(app)

    return app
