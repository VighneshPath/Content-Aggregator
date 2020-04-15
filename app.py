from flask import Flask, render_template, request, session
from flask_session import Session
import content_aggregator
import requests
headers ={
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"
}

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/getparts", methods = ["POST", "GET"])
def getparts():
    if(request.method == "GET"):
        return render_template("error.html", message = "Request Method Get Not Allowed, Please Enter Part Name in previous Page")
    session["category"] = request.form.get("Category_Option")
    session["part_name"] = request.form.get("partname")
    part_list = content_aggregator.get_part_details(session["part_name"],session["category"])
    if(part_list == []):
        return render_template("error.html", message = f'No Part Named {session["part_name"]} Found')
    return render_template("parts.html", part_list = part_list)

