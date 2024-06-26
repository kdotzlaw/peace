# Frontend <--> Flask API <--> Database
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

'''
- Initialize flask app
- Initialize JSON
'''
app = Flask(__name__, template_folder="public")


@app.route("/", methods=["GET"])
def init():
    if request.method == "GET":
        return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        print("POST")


if __name__ == "__main__":
    app.run()
