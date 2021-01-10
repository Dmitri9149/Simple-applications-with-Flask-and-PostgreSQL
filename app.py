from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    words = ["apina", "banaani", "cembalo"]
    return render_template("index.html", message="Tervetuloa", items=words)
#    return "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHellOOOOOOOOOOOOOOOOOO !"

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

@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/result1", methods=["POST"])
def result1():
    pizza = request.form["pizza"]
    extras = request.form.getlist("extra")
    message = request.form["message"]
    return render_template("result1.html", pizza=pizza,
                                          extras=extras,
                                          message=message)
@app.route("/page/<int:id>")
def page():
    return "Tama on sive "+str(id)

@app.route("/pictures")
def pictures():
    return render_template("pictures.html", message="Some picture made by Haskell")

@app.route("/form")
def form():
    return render_template("/form.html")
@app.route("/result", methods=["POST"])
def result(): 
    return render_template("result.html", name = request.form["name"])

