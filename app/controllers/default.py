from app import app
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from app.models import db
@app.route('/')
def index():
    titlePage = db.cursor.execute("SELECT * FROM posts;")
    results = db.cursor.fetchall()
    return render_template('index.html', results=results)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == "POST":
        nome = request.form['nome']
        print(nome)
    return render_template('cadastrar.html')