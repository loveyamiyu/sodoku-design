from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/rules/")
def rules():
    return render_template("rules.html")

@app.route("/stats/")
def stats():
    return render_template("stats.html")
