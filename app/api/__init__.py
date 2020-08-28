from flask import Blueprint
from flask_restx import Api

# bp used for register_blueprint func
bp = Blueprint('api', __name__)

# api_bp is used for attaching routes
api_bp = Api(bp, ordered=True)

from app.api.routes import *
