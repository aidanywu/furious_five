# import "packages" from flask
from flask import Blueprint, render_template, request
import requests
import json
# create a Flask instance
boutus = Blueprint('aboutus', __name__)


@boutus.route("/aboutus/")
def aboutus():
    return render_template("aboutus.html")


@boutus.route("/williamli/")
def williamli():
    return render_template("about/williamli.html")


@boutus.route("/aidanwu/", methods=['GET','POST'])
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


@boutus.route("/williamwu/")
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


@boutus.route("/vaishavijay/")
def vaishavijay():
    return render_template("about/vaishavijay.html")


@boutus.route("/soren/")
def soren():
    return render_template("about/soren.html")
