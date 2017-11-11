from flask import Flask,  render_template , request
from . import app






from flask import Flask, render_template, request
from . import app
user = ""
pw = ""
wrong = "your login was incorrect"
user2 = ""
pw2 = ""
@app.route('/' , methods = ["POST", "GET"])



def index():
   true = "true"
   return render_template('index.html')

@app.route('/login' , methods = ["POST", "GET"])
def login():
    if request.method =="POST":
        global user, pw
        pw = request.form["pw"]
        user = request.form["user"]
        return render_template('login.html' , user2 = user2 , pw2 = pw2)

@app.route('/welcome' , methods = ["POST", "GET"])
def welcome():
    global user, pw
    if request.method =="POST":
        global user, pw, pw2, user2
        pw2 = request.form["pw2"]
        user2 = request.form["user2"]

        if user == user2 and pw == pw2:
            return render_template('welcome.html' , user = user)
        else:
            return render_template('login.html', wrong = wrong)
