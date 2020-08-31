"""
This module creates flask Blueprint for flask routes of this package
"""

from flask import Blueprint

# assigning type Blueprint because mypy don't recognize type
bp: Blueprint = Blueprint(
    "plots",
    __name__,
    template_folder="templates",
    static_folder="static"
)

from app.plots.routes import *
