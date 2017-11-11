




from flask import Flask, render_template, request
from . import app
fname = ""
lname = ""
@app.route('/' , methods = ["POST", "GET"])



def index():
   true = "true"
   return render_template('index.html' , fname = fname , lname = lname)

@app.route('/welcome' , methods = ["POST", "GET"])
def welcome():
    if request.method =="POST":
        global fname, lname
        fname = request.form["fname"]
        lname = request.form["lname"]
        like = request.form["like"]
        if like == "yes":
            return render_template('welcome.html' , fname = fname , lname = lname)
        else:

            return render_template('sad.html' , fname = fname , lname = lname)


    else:
        true = "true"
@app.route('/sad' , methods = ["POST", "GET"])
def sad():
    return render_template('sad.html' , fname = fname)


@app.route('/idc' , methods = ["POST", "GET"])
def idc():
    return render_template('idc.html' , fname = fname)
