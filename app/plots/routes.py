"""
This module defines routes in current blueprint
"""

from flask import render_template

from app.plots import bp


@bp.route("/plots", methods=["GET"])
def plots():
    """
    Returns html with plots from api data
    """
    return render_template("plots.html")
