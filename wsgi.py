import os

from application.app import initialize_app

app = initialize_app(os.environ["FLASK_CONFIG"])
