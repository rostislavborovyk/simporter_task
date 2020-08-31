from flask import render_template

from app.plots import bp


@bp.route("/plots", methods=["GET"])
def plots():
    return render_template("plots.html")
