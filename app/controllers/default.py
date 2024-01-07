from app import app
from flask import Flask
from flask import redirect
from flask import render_template
from app.models import db
@app.route('/')
def index():
    titlePage = db.cursor.execute("SELECT * FROM posts")
    results = db.cursor.fetchall()
    return render_template('index.html', titlePage=results)