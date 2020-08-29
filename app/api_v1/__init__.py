from flask_restx import Namespace

ns = Namespace("api", description="timeline api v1")
from app.api_v1.routes import *
