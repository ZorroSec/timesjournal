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
    db.cursor.execute("SELECT * FROM posts;")
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
        if results:
            classDiv = "alert alert-warning"
            feedback = "Já existe um perfil com estas informações!!"
            return render_template('cadastrar.html', classDiv=classDiv, feedback=feedback)
        else:
            classDiv = "alert alert-success"
            feedback = "Conta criada com sucesso!!"
            link = "/"
            linkInfo = "Voltar para a página inicial."
            # addNewPost = redirect(url_for('/publicar'))
            # buttonAdd = redirect(url_for('/', addNewPost=addNewPost))
            return render_template('cadastrar.html', classDiv=classDiv, feedback=feedback, link=link, linkInfo=linkInfo)
    return render_template('cadastrar.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']
        db.cursor.execute(f"SELECT * FROM users WHERE email = '{email}' and senha = '{senha}'")
        results = db.cursor.fetchall()
        rows = db.cursor.rowcount
        if rows < 1:
            classDiv = "alert alert-danger"
            feedback = "Informacões invalidas."
            return render_template('login.html', classDiv=classDiv, feedback=feedback)
        else:
            return redirect(f"/{results[0][1]}/index")
    return render_template('login.html')

@app.route('/<nome>/index')
def initial(nome):
    db.cursor.execute("SELECT * FROM posts;")
    results = db.cursor.fetchall()
    return render_template('access.html', nome=nome, results=results)

@app.route('/<nome>/publicar', methods=['GET', 'POST'])
def publicar(nome):
    return render_template('publicar.html', nome=nome)