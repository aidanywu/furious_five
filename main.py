# import "packages" from flask
from flask import Flask, render_template
#test
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
    return render_template("williamli.html")


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