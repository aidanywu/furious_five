# import "packages" from flask
from flask import Blueprint, render_template
# create a Flask instance
minigames = Blueprint('minigames', __name__)


@minigames.route("/tictactoe/")
def tictactoe():
    return render_template("minigames/tictactoe.html")


@minigames.route("/rockpaperscissors/")
def rockerpaperscissors():
    return render_template("minigames/rockpaperscissors.html")


@minigames.route("/sleepingsimulator/")
def sleepingsimulator():
    return render_template("minigames/sleepingsimulator.html")

@minigames.route("/spacespam/")
def spacespam():
    return render_template("minigames/spacespam.html")

@minigames.route("/graph/")
def graph():
    return render_template("minigames/graph.html")


@minigames.route("/life/")
def life():
    return render_template("minigames/life.html")


@minigames.route("/snake/")
def snake():
    return render_template("minigames/snake.html")
