from flask import Flask
from api.urls import urls

def run_app(*args, **kwargs):
    # Initialize application
    app = Flask(__name__)

    # Add all routes
    for add_route in urls:
        add_route(app)

    app.run(*args, **kwargs)

    return app