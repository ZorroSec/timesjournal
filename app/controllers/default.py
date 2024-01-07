from app import app
from flask import Flask
from flask import redirect
from flask import render_template

@app.route('/')
def index():
    return 'Index page'