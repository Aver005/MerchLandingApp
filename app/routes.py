from flask import render_template, redirect, session, request
from run import app


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def welcome_landing_page():
    return render_template("/pages/landing.html")
