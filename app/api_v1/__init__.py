"""
This module creates flask_restx Namespace for api routes of this package
"""

from flask_restx import Namespace

# assigning type Namespace because mypy don't recognize type
ns: Namespace = Namespace("api", description="timeline api v1")

from app.api_v1.routes import *
