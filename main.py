from flask import Flask, redirect, url_for, render_template
import Data, scraping
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
    return render_template("gg-covid.html", data=scraping.brazildata(), data1=scraping.worldtotal())

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


#===================================================================================

@app.route("/africa")
@app.route("/")
def africa():
    return render_template("history-africa.html")

@app.route("/america")
@app.route("/")
def america():
    return render_template("history-america.html")

@app.route("/brazil")
@app.route("/")
def brazil():
    return render_template("history-brazil.html")

@app.route("/denmark")
@app.route("/")
def denmark():
    return render_template("history-denmark.html")

@app.route("/greece")
@app.route("/")
def greece():
    return render_template("history-greece.html")

@app.route("/iceland")
@app.route("/")
def iceland():
    return render_template("history-iceland.html")

@app.route("/india")
@app.route("/")
def india():
    return render_template("history-india.html")

#===================================================================================


if __name__ == "__main__":
    app.run(debug=True)
