from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    sql = "SELECT id, topic, created_at FROM polls ORDER BY id DESC"
    result = db.session.execute(sql)
    polls = result.fetchall()
    return render_template("index.html", polls=polls)

@app.route("/new")
def new():
    return render_template("new.html")

