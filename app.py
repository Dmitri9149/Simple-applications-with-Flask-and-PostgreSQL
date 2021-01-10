from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<b>Tervetuloa</b> <i>sovellukseen</i>"

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


