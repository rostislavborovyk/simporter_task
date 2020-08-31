from flask import Blueprint

bp = Blueprint(
    "plots",
    __name__,
    template_folder="templates",
    static_folder="static"
)

from app.plots.routes import *
