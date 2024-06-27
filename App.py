# Frontend <--> Flask API <--> Database
from flask import Flask, render_template, request, send_from_directory
# from backend import db
import os

'''
- Initialize flask app
- Initialize JSON
'''
app = Flask(__name__)

reactFolder = 'frontend'
directory = os.getcwd() + f'/{reactFolder}/build/static'

'''
METHOD: index()
PRE-CONDITION: None.
POST-CONDITION: Serve user the login.html file.
'''
@app.route('/')
def index():
    path = os.getcwd() + f'/{reactFolder}/build'
    return send_from_directory(directory=path, path='index.html')

'''
METHOD: serve()
PRE-CONDITION: None.
POST-CONDITION: Serve the requested file within the static folder.
'''
@app.route('/static/<folder>/<file>')
def serve(folder, file):
    path = folder + '/' + file
    return send_from_directory(directory=directory, path=path)



'''
METHOD: login()
PRE-CONDITION: given a JSON HTTP POST request with username, pass, db, host ip
POST-CONDITION: connection to db is established if successful, prompt re-login if unsuccessful
'''

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

'''
if __name__ == "__main__":
    app.run(host="localhost", port=3000)
