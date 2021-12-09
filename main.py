# import "packages" from flask
from flask import Flask, render_template
import requests
import json
#test
#another test
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
    return render_template("about/williamL.html")


@app.route("/aidanwu/")
def aidanwu():
    return render_template("about/aidanW.html")


@app.route("/worldclock/")
def worldclock():
    url = "https://world-clock.p.rapidapi.com/json/pst/now"
    headers = {
        'x-rapidapi-host': "world-clock.p.rapidapi.com",
        'x-rapidapi-key': "1d9c0e5dd4msh00cea2fa8d7699fp1dfecdjsn1cf8da6644a9"
    }
    response = requests.request("GET", url, headers=headers)
    time = json.loads(response.text)
    return render_template("worldclock.html", query=time)

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