from flask import Flask, render_template, request
import content_aggregator

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/part", methods = ["POST"])
def enterpart():
    global category
    category = request.form.get("Category_Option")
    return render_template("part.html",category = category)

@app.route("/getparts", methods = ["POST"])
def getparts():
    global part_name
    part_name = request.form.get("partname")
    part_list = content_aggregator.get_part_details(part_name,category)
    return render_template("parts.html", part_list = part_list)

