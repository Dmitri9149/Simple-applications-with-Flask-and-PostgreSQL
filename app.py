from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    words = ["apina", "banaani", "cembalo"]
    return render_template("index.html", message="Tervetuloa", items=words)

@app.route("/page1")
def page1():
    return "Tämä on Page1"

@app.route("/page2")
def page2():
    return "Tama on Page2"

@app.route("/test")
def test():
    content = ""
    for i in range(1,101):
        content += str(i)+" "
    return content

@app.route("/page/<int:id>")
def page():
    return "Tama on sive "+str(id)


