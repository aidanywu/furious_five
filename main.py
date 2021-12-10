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
def index():
    return render_template("index.html")


@app.route("/aboutus/")
def aboutus():
    return render_template("aboutus.html")


@app.route("/williamli/")
def williamli():
    return render_template("about/williamli.html")


@app.route("/aidanwu/", methods=['GET','POST'])
def aidanwu():
    # time api
    url = "https://world-clock.p.rapidapi.com/json/pst/now"
    headers = {
        'x-rapidapi-host': "world-clock.p.rapidapi.com",
        'x-rapidapi-key': "1d9c0e5dd4msh00cea2fa8d7699fp1dfecdjsn1cf8da6644a9"
    }
    response = requests.request("GET", url, headers=headers)
    time = json.loads(response.text)
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
    return render_template("about/aidanwu.html", query=time, data=data, word=querystring1["word"])


@app.route("/williamwu/")
def williamwu():
    return render_template("about/williamwu.html")


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


@app.route('/gamesapi/', methods=['GET', 'POST'])
def gamesapi():
    url = "https://free-to-play-games-database.p.rapidapi.com/api/games"
    querystring = {"platform":"all","sort-by":"alphabetical"}
    headers = {
        'x-rapidapi-host': "free-to-play-games-database.p.rapidapi.com",
        'x-rapidapi-key': "99055c6785msh0eec04755216d76p1d458djsnf1bc6a1c3b66"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    if request.form:
        platform = request.form.get("platform")
        category = request.form.get("category")
        if platform == "all" and category == "all":
            querystring = {"platform":"all","sort-by":"alphabetical"}
            response = requests.request("GET", url, headers=headers, params=querystring)
            data = json.loads(response.text)
            return render_template("gamesapi.html", games=data, length=len(data), query=querystring, category=False)
    elif platform == "all" and category == "shooter":
        querystring = {"platform":"all","category":"shooter","sort-by":"alphabetical"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)
        return render_template("gamesapi.html", games=data, length=len(data), query=querystring, category=True)
    elif platform == "all" and category == "strategy":
        querystring = {"platform":"all","category":"strategy","sort-by":"alphabetical"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)
        return render_template("gamesapi.html", games=data, length=len(data), query=querystring, category=True)
    elif platform == "browser" and category == "all":
        querystring = {"platform":"browser","sort-by":"alphabetical"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)
        return render_template("gamesapi.html", games=data, length=len(data), query=querystring, category=False)
    elif platform == "browser" and category == "shooter":
        querystring = {"platform":"browser","category":"shooter","sort-by":"alphabetical"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)
        return render_template("gamesapi.html", games=data, length=len(data), query=querystring, category=True)
    elif platform == "browser" and category == "strategy":
        querystring = {"platform":"browser","category":"strategy","sort-by":"alphabetical"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)
        return render_template("gamesapi.html", games=data, length=len(data), query=querystring, category=True)
    elif platform == "pc" and category == "all":
        querystring = {"platform":"pc","sort-by":"alphabetical"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)
        return render_template("gamesapi.html", games=data, length=len(data), query=querystring, category=False)
    elif platform == "pc" and category == "shooter":
        querystring = {"platform":"pc","category":"shooter","sort-by":"alphabetical"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)
        return render_template("gamesapi.html", games=data, length=len(data), query=querystring, category=True)
    elif platform == "pc" and category == "strategy":
        querystring = {"platform":"pc","category":"strategy","sort-by":"alphabetical"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)
        return render_template("gamesapi.html", games=data, length=len(data), query=querystring, category=True)
    return render_template("gamesapi.html", games=data, length=len(data), query=querystring, category=False)

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
