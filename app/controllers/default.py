from app import app
from flask import Flask
from flask import redirect
from flask import render_template
from flask import url_for
from flask import request
from datetime import date
from app.models import db
import unicodedata
@app.route('/')
def index():
    titlePage = db.cursor.execute("SELECT * FROM posts;")
    results = db.cursor.fetchall()
    return render_template('index.html', results=results)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == "POST":
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        data__atual = date.today()
        # db.cursor.execute(f"INSERT INTO users(nome,email,senha,data,status) VALUES('{nome}','{email}','{senha}','{data__atual}','')")
        # db.conn.commit()
        # results = db.cursor.rowcount
        # print(results)
        # # return "<script>alert('Cadastro realizado com sucesso!!')</script>"
        # redirect('/')
        checkExistUser = db.cursor.execute(f"SELECT * FROM users WHERE nome = '{nome}' and email = '{email}'")
        results = db.cursor.fetchall()
        if(results):
            classDiv = "alert alert-warning"
            feedback = "Já existe um perfil com estas informações!!"
            return render_template('cadastrar.html', classDiv=classDiv, feedback=feedback)
        else:
            classDiv = "alert alert-success"
            feedback = "Conta criada com sucesso!!"
            link = "/"
            linkInfo = "Voltar para a página inicial."
            return render_template('cadastrar.html', classDiv=classDiv, feedback=feedback, link=link, linkInfo=linkInfo)
    return render_template('cadastrar.html')