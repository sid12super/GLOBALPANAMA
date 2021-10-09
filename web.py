from flask import Flask , render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/about")
def sid():
    name = "****"
    return render_template("about.html", name2 = name)


@app.route("/nf")
def nfi():
    return render_template("nf.html")


app.run(debug=True)