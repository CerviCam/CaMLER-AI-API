from flask import Flask
from api.urls import urls

def create_app():
    # Initialize application
    app = Flask(__name__)

    # Add all routes
    for add_route in urls:
        add_route(app)

    return app