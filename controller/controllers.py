import random
from flask import Blueprint, render_template, request, redirect, session
from model.models import User
import load_excel

main = Blueprint('main', __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        session["token"] = str(random.randint(1, 1000))
        return render_template("index.html", token=session["token"])
    else:
        email = request.form.get("email")
        password = request.form.get("password")
        token = request.form.get("token")

        if token != session["token"]:
            return redirect("/")

        login_info = User.get_login_info()
        if email == login_info.email and password == login_info.password:
            session["loginUser"] = email
            return redirect("/main")
        else:
            return redirect("/")


@main.route("/main", methods=["GET"])
def list():
    if 'loginUser' not in session:
        return redirect("/")
    data = load_excel.load_excel("./persons.xlsx")
    return render_template("main.html", data=data)


@main.route("/logout", methods=["GET", "POST"])
def logout():
    if request.method == "GET":
        return render_template("logout.html")
    else:
        session.pop("loginUser", None)
        return redirect("/")
