# import "packages" from flask
from flask import Blueprint, render_template
# create a Flask instance
notebooks = Blueprint('notebooks', __name__)


@notebooks.route("/notebook1/")
def notebook1():
    return render_template("notebooks/notebook1.html")


@notebooks.route("/notebook2/")
def notebook2():
    return render_template("notebooks/notebook2.html")


@notebooks.route("/notebook3/")
def notebook3():
    return render_template("notebooks/notebook3.html")


@notebooks.route("/wCalendar/")
def wCalendar():
    return render_template("notebooks/weekly calendar.html")
