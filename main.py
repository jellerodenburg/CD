# Import what we need from flask
from flask import Flask, redirect, render_template

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route("/")
def index():
    return "Hello, this is the CD test app!"


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/cow")
def cow():
    return "MOoooOo!"


@app.route("/home")
def home():
    return redirect("/", code="302")


@app.route("/links")
def links():
    return render_template("links.html", title="Links")
