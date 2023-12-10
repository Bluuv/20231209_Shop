import os
import multiprocessing

from flask import Flask, redirect, render_template
from werkzeug.security import check_password_hash, generate_password_hash
import stdiomask

# Configure application
# shop = Flask(__name__)

userDictList = []
session = {}

# @shop.route("/register", methods=["GET", "POST"])
def register():
    # if request.method == "POST":

        
        username = input("Username: ")
        password = stdiomask.getpass()
        confirmation = stdiomask.getpass()

        if not password or password!=confirmation:
            print ("Please provide a valid password that matches its confirmation.")
        else:
            userDict = {
                        "username": username,
                        "password": password
                        }
            userDictList.append(userDict)
            # print(f"Your username is {username} and your password is {password}")
            # print(userDict)
            # print(userDictList)

# @shop.route("/login", methods=["GET", "POST"])
def login():

    print()
    print("PLAESE LOG IN")
    print()
    username = input("Username: ")
    password = stdiomask.getpass()

    # foundUsername = []
    # foundPass = []
    # for element in userDictList:
    #     if element["username"]==username:
    #         foundUsername.append(username)
    # for element in userDictList:
    #     if element["password"]==password:
    #         foundUsername.append(password)

    for dictionary in userDictList:
        if username in dictionary.values():
            if password == dictionary["password"]:
                print("You are logged in!")
                session["username"]=username
                session["password"]=password
                return session
            else:
                print("Incorrect Username or Password")
                return 0
    print("Incorrect Username or Password")
    return 0

    # print(list(filter(lambda item: item["username"]==username, userDictList))[0]['username'])

    #####

    # if not foundUsername or not foundPass:
    #     print("Incorrect Username or Password")
    # else:
    #     print("You are logged in!")

    # print(f"foundUsername: {foundUsername}")
    # print(f"foundPass: {foundPass}")
    # return username, password

# @shop.route("/logout")
def logout():
    session.clear()


if __name__=="__main__":
    # shop.run(debug=True)
    for i in range(1):
        register()
    login()

