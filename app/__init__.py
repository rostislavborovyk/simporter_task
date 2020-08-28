from importlib import import_module

from flask import Flask
from flask_restx import Api

api = Api()


def register_blueprints(app: Flask) -> None:
    api_bp = import_module("app.api").bp
    app.register_blueprint(api_bp, url_prefix='/api')


def register_extensions(app: Flask) -> None:
    api.init_app(app)


def create_app(config_class=None) -> Flask:
    app = Flask(__name__)
    register_extensions(app)
    register_blueprints(app)
    return app
