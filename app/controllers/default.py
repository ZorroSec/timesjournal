from app import app
from flask import Flask
from flask import redirect
from flask import render_template

@app.route('/')
def index():
    titlePage = 'TimesJournal'
    return render_template('index.html', titlePage=titlePage)