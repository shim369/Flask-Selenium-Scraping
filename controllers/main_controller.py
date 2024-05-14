import random
from flask import Blueprint,render_template,request,redirect,session
import load_excel

main = Blueprint('main',__name__)

@main.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        token = random.randint(1, 1000)
        session["token"] = str(token)

        return render_template("index.html",token=token)
    else:
        email = request.form.get("email")
        password = request.form.get("password")
        token = request.form.get("token")

        if token != str(session["token"]):
            return redirect("/")
    
    login_info = {"email": "shim@gmail.com", "password": "abcd1234"}

    if email == login_info["email"] and password == login_info["password"]:
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

@main.route("/logout", methods=["GET","POST"])
def form():
    if request.method == "GET":
        return render_template("logout.html")
    else:
        session.pop("loginUser", None)
        return redirect("/")
    