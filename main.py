from flask import Flask, render_template, url_for, request, redirect
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
    return render_template("gg-covid.html", data=scraping.countrydata(), data1=scraping.worldtotal())

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

@app.route('/1', methods=["GET", "POST"])
def continentcheck1():
    if request.method == "POST":
        form = request.form
        Con1 = form["Continent1"]
        if Con1 == "Asia" or Con1 == "asia":
            var1 = 'Continent Correct!'
            return render_template("geoguesser.html", Continent=var1,data=Data.inputdata1(),data1=Data.inputdata2(), data2=Data.picran())
        else:
            var1 = 'Continent Incorrect!'
            return render_template("geoguesser.html", Continent=var1,data=Data.inputdata1(),data1=Data.inputdata2(), data2=Data.picran())
@app.route('/c1', methods=["GET", "POST"])
def countrycheck1():
    if request.method == "POST":
        form = request.form
        Coun1 = form["Country1"]
        if Coun1 == "India" or Coun1 == "india":
            var2 = 'Country Correct!'
            return render_template("geoguesser.html", Country=var2,data=Data.inputdata1(),data1=Data.inputdata2(), data2=Data.picran())
        else:
            var2 = 'Country Incorrect!'
            return render_template("geoguesser.html", Country=var2,data=Data.inputdata1(),data1=Data.inputdata2(), data2=Data.picran())
@app.route('/C1', methods=['GET', 'POST'])
def citycheck1():
    if request.method == "POST":
        form = request.form
        City = form['City1']
        if City == "Agra" or City == "agra":
            var3 = 'City Correct!'
            return render_template("geoguesser.html", City=var3,data=Data.inputdata1(),data1=Data.inputdata2(), data2=Data.picran())
        else:
            var3 = 'City Incorrect!'
            return render_template("geoguesser.html", City=var3,data=Data.inputdata1(),data1=Data.inputdata2(), data2=Data.picran())
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
    app.run(debug=True, host="127.0.0.1", port="5001")
