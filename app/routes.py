from flask import render_template
from app import app

@app.route("/")
@app.route("/index", methods=["GET", "POST"])
def index():
    user = {
        "username" : "SomeUsername", 
        "age" : "27" }
    return render_template("index.html", title="Home", user=user)

@app.route("/register")
def register():
    return render_template("register.html", title="Create New User Login")