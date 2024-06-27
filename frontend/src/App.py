# Frontend <--> Flask API <--> Database
import flask
from flask import Flask, render_template, request
import db

'''
- Initialize flask app
- Initialize JSON
'''
app = Flask(__name__, template_folder="../templates", static_folder="/static")


@app.route("/")
def init():
    print("rendering")
    return render_template("login.html")


'''
METHOD: login()
PRE-CONDITION: given a JSON HTTP POST request with username, pass, db, host ip
POST-CONDITION: connection to db is established if successful, prompt re-login if unsuccessful
'''


@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        host = request.form["host"]
        database = request.form["db"]
        # Attempt DB connection
        # if valid login (ie cnxn to db is successful), load home.html template
        if db.init(host, username, password, database):
            resp = flask.make_response()
            resp.status_code = 200
            resp.data = "Logged in"
            return resp

            # resp = make_response(render_template("home.html"))


if __name__ == "__main__":
    app.run(host="localhost",port=3000)
