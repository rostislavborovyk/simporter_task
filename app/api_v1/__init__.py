"""
This module creates flask_restx Namespace for api routes of this package
"""

from flask_restx import Namespace

ns = Namespace("api", description="timeline api v1")
from app.api_v1.routes import *
