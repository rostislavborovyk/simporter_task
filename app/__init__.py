"""
This module initializes api object and defines create_app function
"""

from flask import Flask
from flask_restx import Api

api = Api(
    ordered=True,
    title="api_v1",
    version='1.0',
    description='API for timeline data',
    doc="/api/info/"
)


def _add_namespaces(api: Api) -> None:
    from app.api_v1 import ns as ns1
    api.add_namespace(ns1)


def _register_blueprints(app: Flask) -> None:
    from app.plots import bp as plots_bp
    app.register_blueprint(plots_bp)


def create_app() -> Flask:
    app = Flask(__name__)
    api.init_app(app)
    _add_namespaces(api)
    _register_blueprints(app)
    return app
