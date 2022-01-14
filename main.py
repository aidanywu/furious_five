# import "packages" from flask
from flask import Flask, render_template, request
from templates.about.aboutus import boutus
from templates.notebooks.notebooks import notebooks
from templates.studyrooms.studyrooms import studyrooms
from templates.minigames.minigames import minigames
import requests
import json
# test
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


@app.route("/aboutus/")
def aboutus():
    return render_template("aboutus.html")


@app.route("/williamli/")
def williamli():
    return render_template("about/williamli.html")


@app.route("/aidanwu/", methods=['GET', 'POST'])
def aidanwu():
    # dictionary api
    url1 = "https://dictionary-by-api-ninjas.p.rapidapi.com/v1/dictionary"
    querystring1 = {"word": "word"}
    if request.form:
        word = request.form.get("word")
        if len(word) != 0:  # input field has content
            querystring1["word"] = word
    headers1 = {
        'x-rapidapi-host': "dictionary-by-api-ninjas.p.rapidapi.com",
        'x-rapidapi-key': "1d9c0e5dd4msh00cea2fa8d7699fp1dfecdjsn1cf8da6644a9"
    }
    response1 = requests.request("GET", url1, headers=headers1, params=querystring1)
    data = json.loads(response1.text)
    return render_template("about/aidanwu.html", data=data, word=querystring1["word"])


@app.route("/williamwu/")
def williamwu():
    # time api
    url = "https://world-clock.p.rapidapi.com/json/pst/now"
    headers = {
        'x-rapidapi-host': "world-clock.p.rapidapi.com",
        'x-rapidapi-key': "1d9c0e5dd4msh00cea2fa8d7699fp1dfecdjsn1cf8da6644a9"
    }
    response = requests.request("GET", url, headers=headers)
    time = json.loads(response.text)
    return render_template("about/williamwu.html", query=time)


@app.route("/vaishavijay/")
def vaishavijay():
    return render_template("about/vaishavijay.html")


@app.route("/soren/")
def soren():
    return render_template("about/soren.html")


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


@app.route("/cafe/")
def cafe():
    return render_template("studyrooms/cafe.html")


@app.route("/naturesounds/")
def naturesounds():
    if request.form:
        spotify = request.form.get("spotify")
        if len(name) != 0:  # input field has content
            return render_template("studyrooms,naturesounds.html", spotify=spotify)
    return render_template("studyrooms/naturesounds.html", spotify='https://open.spotify.com/artist/4NqS7DbPFYwZmniGHCPMpm?utm_source=generator&theme=0')


@app.route("/subjects/notebook3/")
def notebook3():
    return render_template("notebooks/notebook3.html")


@app.route("/subjects/notebook1/")
def notebook1():
    return render_template("notebooks/notebook1.html")


@app.route("/subjects/notebook2/")
def notebook2():
    return render_template("notebooks/notebook2.html")


@app.route("/tictactoe/")
def tictactoe():
    return render_template("minigames/tictactoe.html")


@app.route("/rockpaperscissors/")
def rockerpaperscissors():
    return render_template("minigames/rockpaperscissors.html")


@app.route("/sleepingsimulator/")
def sleepingsimulator():
    return render_template("minigames/sleepingsimulator.html")


@app.route("/darkmode/")
def darkmode():
    return render_template("darkmode.html")


@app.route("/feedback/")
def feedback():
    return render_template("feedback.html")


@app.route("/subjects/")
def subjects():
    return render_template("subjects.html")


@app.route("/math/")
def math():
    return render_template("subjects/math.html")


@app.route("/subjects/calculator/")
def calculator():
    return render_template("calculator.html")


@app.route("/english/")
def english():
    return render_template("english.html")


@app.route("/science/")
def science():
    return render_template("science.html")


@app.route("/subjects/colors/")
def colors():
    return render_template("colors.html")


@app.route("/subjects/art/")
def art():
    return render_template("art.html")

# runs the application on the development server


if __name__ == "__main__":
    app.run(debug=True)
