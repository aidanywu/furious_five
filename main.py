# import "packages" from flask
from flask import Flask, render_template, request
<<<<<<< Updated upstream
from templates.about.aboutus import boutus
from templates.notebooks.notebooks import notebooks
from templates.studyrooms.studyrooms import studyrooms
from templates.minigames.minigames import minigames
=======
import requests
import json
from __init__ import app

from starter.starter import app_starter
from algorithm.algorithm import app_algorithm
from api.webapi import app_api
from templates.crud.app_crud import app_crud
from templates.crud.app_crud_api import app_crud_api
from y2022 import app_y2022

app.register_blueprint(app_starter)
app.register_blueprint(app_algorithm)
app.register_blueprint(app_api)
app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)
app.register_blueprint(app_y2022)

# test
>>>>>>> Stashed changes
# create a Flask instance
app = Flask(__name__)
app.register_blueprint(boutus)
app.register_blueprint(notebooks)
app.register_blueprint(studyrooms)
app.register_blueprint(minigames)


# connects default URL to render index.html
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/timer/")
def timer():
    return render_template("timer.html")



@app.route("/wCalendar/")
def wCalendar():
    return render_template("notebooks/weekly calendar.html")


@app.route("/foff/")
def foff():
    link = "https://rapidapi.com/community/api/foaas/"
    return render_template("about/easteregg.html")


@app.route("/darkmode/")
def darkmode():
    return render_template("darkmode.html")


@app.route("/feedback/")
def feedback():
    return render_template("feedback.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
