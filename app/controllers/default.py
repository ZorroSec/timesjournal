from app import app
from flask import Flask
from flask import redirect
from flask import render_template
from flask import url_for
from flask import request
from datetime import date
from app.models import db
import unicodedata
import markdown

@app.route('/')
def index():
    db.cursor.execute("SELECT * FROM post;")
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
            newUsername = nome.lower().replace(' ', '')
            db.cursor.execute(f"INSERT INTO users(nome,email,senha,data) VALUES('{newUsername}','{email}','{senha}','{data__atual}')")
            result = db.conn.commit()
            print(result)
            classDiv = "alert alert-success"
            feedback = "Conta criada com sucesso!!"
            print(results)
            link = f"/"
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
    db.cursor.execute(f"SELECT * FROM users WHERE nome = '{nome}'")
    result = db.cursor.fetchall()
    rows = db.cursor.rowcount
    if rows < 1:
        return render_template('error/user.html')
    else:
        db.cursor.execute("SELECT * FROM post ORDER BY id DESC;")
        results = db.cursor.fetchall()
        return render_template('access.html', nome=nome, results=results)


@app.route('/<nome>/publicar', methods=['GET', 'POST'])
def publicar(nome):
    db.cursor.execute(f"SELECT * FROM users WHERE nome = '{nome}'")
    results = db.cursor.fetchall()
    rows = db.cursor.rowcount
    if rows < 1:
        return render_template('error/user.html')
    else:
        db.cursor.execute("SELECT * FROM post;")
        result = db.cursor.fetchall()
        if request.method == 'POST':
            titulo = request.form['titulo']
            post = request.form['post']
            fonte = request.form['fonte']
            data__atual = date.today()
            db.cursor.execute(f"INSERT INTO post(likes,nome,titulo,post,data,fonte) VALUES('1','{nome}','{titulo}','{post}','{data__atual}','{fonte}')")
            commit = db.conn.commit()
            print(commit)
            if commit:
                db.cursor.execute(f"SELECT * FROM post")
                result = db.cursor.fetchall()
                print(result)
                return redirect(f'/{result[0][2]}/{result[0][3]}')
        return render_template('publicar.html', nome=nome)


@app.route('/<nome>/<titulo>')
def post(nome, titulo):
    db.cursor.execute(f"SELECT * FROM post WHERE nome = '{nome}' and titulo = '{titulo}'")
    postInfo = db.cursor.fetchall()
    return render_template('post.html', post=postInfo)