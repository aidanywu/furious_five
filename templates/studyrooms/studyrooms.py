# import "packages" from flask
from flask import Blueprint, render_template, request
# create a Flask instance
studyrooms = Blueprint('studyrooms', __name__)


@studyrooms.route("/cafe/")
def cafe():
    return render_template("studyrooms/cafe.html")


@studyrooms.route("/naturesounds/", methods=['GET','POST'])
def naturesounds():
    if request.form:
        spotify = request.form.get("spotify")
        if len(spotify) != 0:  # input field has content
            return render_template("studyrooms/naturesounds.html", spotify=spotify)
    return render_template("studyrooms/naturesounds.html", spotify='https://open.spotify.com/embed/playlist/37i9dQZF1DX4PP3DA4J0N8?utm_source=generator')
