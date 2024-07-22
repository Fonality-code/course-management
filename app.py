from flask import Flask, redirect, url_for, render_template
from config import config


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calendar")
def calendar():
    return render_template("calendar.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/signup")
@app.route("/register")
def signup():
    return render_template("auth/signup.html")


@app.route("/signin")
@app.route("/login")
def signin():
    return render_template("auth/signin.html")
