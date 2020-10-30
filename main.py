from flask import Flask, redirect, url_for, render_template
import Data
app = Flask(__name__)

@app.route("/landing")
@app.route("/")
def landing():
    return render_template("gg-landing.html")

@app.route("/home")
@app.route("/")
def home():
    return render_template("gg-home.html")

@app.route("/covid")
@app.route("/")
def covid():
    return render_template("gg-covid.html")

@app.route("/p5")
@app.route("/")
def p5():
    return render_template("gg-p5.html")

@app.route("/history")
@app.route("/")
def history():
    return render_template("gg-history.html")

@app.route("/geoguesser")
def geoguesser():
    return render_template("geoguesser.html", data=Data.inputdata1(), data1=Data.inputdata2(), data2=Data.picran())




if __name__ == "__main__":
    app.run(debug=True)
