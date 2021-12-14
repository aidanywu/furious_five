# import "packages" from flask
from flask import Flask, render_template, request
import requests
import json

# test
# another test
# create a Flask instance
app = Flask(__name__)


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


@app.route("/aidanwu/", methods=['GET','POST'])
def aidanwu():
    # dictionary api
    url1 = "https://dictionary-by-api-ninjas.p.rapidapi.com/v1/dictionary"
    querystring1 = {"word":"word"}
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


@app.route("/foff/")
def foff():
    link = "https://rapidapi.com/community/api/foaas/"
    return render_template("about/easteregg.html")


@app.route("/cafe/")
def cafe():
    return render_template("studyrooms/cafe.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)

finalpage = 586
initialpage = 571

value = finalpage - initialpage + 1
if value > 10:
    print("yea its over bro")
else:
    print("you only have " + value + "pages of notes!")
