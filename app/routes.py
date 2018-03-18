from flask import render_template, request
from app import app
from app.forms import LoginForm

@app.route("/")
@app.route("/index", methods=["GET", "POST"])
def index():
    data = request.form
    print("form data", data)
    user = {
        "username" : ""}
    return render_template("index.html", title="Home", user=user)

@app.route("/register")
def register():
    return render_template("register.html", title="Create New User Login")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", title="Sign In", form=form)