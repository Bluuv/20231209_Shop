import os
import sqlite3

from flask import Flask, redirect, render_template, session, request
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import stdiomask

# Configure application
shop = Flask(__name__)

#Configure session to use filesystem (instead of signed cookies)
shop.config["SESSION_PERMANENT"] = False
shop.config["SESSION_TYPE"] = "filesystem"
Session(shop)

db = sqlite3.connect("shop")


#Endpoints

@shop.route("/")
def index():
    return render_template("register.html")

@shop.route("/register", methods=["GET", "POST"])
def register():
    session.clear()

    if request.method == "POST":
        
        username = request.form.get("username")
        user = db.execute("SELECT * FROM users WHERE username=?", username)
        if not username or len(user)!=0:
            return ("Username already in use or is empty")
        
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not passsword or password!=confirmation:
            return ("Please provide a valid password that matches its confirmation.")

        db.execute("INSERT INTO users(username, hash) VALUES (?, ?)", username, generate_password_hash(password))
        return redirect("/login")
    else:
        return render_template("register.html")

@shop.route("/login", methods=["GET", "POST"])
def login():

    session.clear()
    if request.method == "POST":

        if not request.form.get("username"):
            return ("Please provide username")
        if not request.form.get("password"):
            return ("Please provide password")
        
        userInfo = db.execute("SELECT * FROM users where username=?", request.form.get("username"))

        #Ensure username exists and password is correct
        if len(userInfo)!=1 or not check_password_hash(userInfo[0]["hash"], request.form("password")):
            return("Invalid username or password")
        
        session["user_id"] = userInfo[0]["id"]

        #TODO You will have to change the redirect here to the main page
        return redirect("/")
    else:
        return render_template("login.html")



@shop.route("/logout")
def logout():
    session.clear()

    return redirect("/login")


