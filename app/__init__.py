from flask import Flask
from flask_restx import Api

api = Api(
    ordered=True,
    title="api_v1",
    version='1.0',
    description='A sample API',
    doc="/api/info/"
)


def add_namespaces(api: Api) -> None:
    from app.api_v1 import ns as ns1
    api.add_namespace(ns1)


def register_blueprints(app: Flask) -> None:
    from app.plots import bp as plots_bp
    app.register_blueprint(plots_bp)


# todo add docs to all


def create_app():
    app = Flask(__name__)
    api.init_app(app)
    add_namespaces(api)
    register_blueprints(app)
    return app
