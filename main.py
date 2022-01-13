# import "packages" from flask
from flask import Flask, render_template, request
from templates.about.aboutus import boutus
from templates.notebooks.notebooks import notebooks
from templates.studyrooms.studyrooms import studyrooms
from templates.minigames.minigames import minigames
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
