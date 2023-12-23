import os
import sqlite3
import base64

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

# Connect to the SQLite database (this will create a new database file if it doesn't exist)
db = sqlite3.connect("shop", check_same_thread=False)
# Create a cursor object to interact with the database
cursor=db.cursor()

def getSelectData(query, queryList):

    cursor.execute(query, queryList)
    column_names = [description[0] for description in cursor.description]
    results=cursor.fetchall()
    results_dicts = [dict(zip(column_names, row)) for row in results]
    return results_dicts
    
items=[]



#Endpoints

@shop.route("/")
def index():
    global items
    items=getSelectData("SELECT * FROM products", [])
    for element in items:
        img_base64= base64.b64encode(element["photo"]).decode('utf-8')
        element["photo"]=img_base64
    return render_template("index.html", items=items)


@shop.route("/item")
def item():
    item_id = request.args.get('item', '')
    return render_template("item.html", item_id=item_id)

@shop.route("/register", methods=["GET", "POST"])
def register():
    session.clear()

    if request.method == "POST":
        
        username = request.form.get("username")
        user = getSelectData("SELECT * FROM users WHERE username=?", [username])
        if not username or len(user)!=0:
            return ("apology.html")
        
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not password or password!=confirmation:
            return ("apology.html")
        else:
            cursor.execute("INSERT INTO users(username, hash) VALUES (?, ?)", [username, generate_password_hash(password)])
            db.commit()
            return redirect("/login")

    else:
        return render_template("register.html")



@shop.route("/login", methods=["GET", "POST"])
def login():

    session.clear()
    if request.method == "POST":

        if not request.form.get("username"):
            return ("apology.html")
        if not request.form.get("password"):
            return ("apology.html")
        
        userInfo = getSelectData("SELECT * FROM users where username=?", [request.form.get("username")])

        #Ensure username exists and password is correct
        if len(userInfo)!=1 or not check_password_hash(userInfo[0]["hash"], request.form.get("password")):
            return("apology.html")
        
        session["user_id"] = userInfo[0]["id"]
        session["username"] = userInfo[0]["username"]
        session["money"] = userInfo[0]["money"]
       
        return render_template("index.html", userInfo=userInfo)
    else:
        return render_template("login.html")



@shop.route("/logout")
def logout():
    session.clear()

    return redirect("/login")

@shop.route("/account", methods=["GET", "POST"])
def account():
    if request.method=="GET":
        return render_template("account.html")
    else:
        addmoney=request.form.get("addmoney")
        userinfo=getSelectData("SELECT * from users WHERE username=?", [session["username"]]) 
        moneysum=float(addmoney)+float(userinfo[0]["money"])
        cursor.execute("UPDATE users SET money=? WHERE id=?", [moneysum, session["user_id"]])
        db.commit()
        session["money"] = moneysum
        session["fictionalmoney"] = moneysum
        return render_template("success.html")
    
@shop.route("/cart", methods=["GET", "POST"])
def cart():
    if request.method=="GET":
        return render_template("cart.html")






