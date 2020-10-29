from flask import Flask, redirect, url_for, render_template

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

@app.route("/geo")
@app.route("/")
def geo():
    return render_template("gg-geo.html")

@app.route("/p5")
@app.route("/")
def p5():
    return render_template("gg-p5.html")

@app.route("/history")
@app.route("/")
def history():
    return render_template("gg-history.html")




if __name__ == "__main__":
    app.run(debug=True)
