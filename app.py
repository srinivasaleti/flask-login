from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from model.user import User
from config.config import get_db_session

app = Flask(__name__)


@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]

        session = get_db_session()
        login = session.query(User).filter(User.username == uname and User.password == passw).first()
        session.close()
        if login is not None:
            return redirect(url_for("home"))
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        mail = request.form['mail']
        passw = request.form['passw']
        session = get_db_session()
        register = User(username=uname, email=mail, password=passw)
        session.add(register)
        session.commit()
        session.close()
        return redirect(url_for("login"))
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
