import pytest


from application.app import initialize_app
from application.models import db


@pytest.fixture
def app():
    app = initialize_app("testing")

    return app


@pytest.fixture(scope="function")
def database(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

    yield db
