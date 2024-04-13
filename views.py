from flask import render_template, request, redirect, session, flash, url_for

import models
from app import app

@app.route('/')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

app.route('/valida')
def validacao():
    usuario = models.info.query.filter_by(nickname=request.form['nome']).first()
    if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname+'logado com sucesso')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)

@app.route('/lista')
def lista():
    return render_template('lista.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
@app.route('/criar', methods = ['POST',])
def cadastrar():
   nome = request.form['nome']
   cpf = request.form['password']
   email = request.form['email']
   dado = models.info.query.filter_by(nome=nome).first()
   if info:
       flash('Jogo já existente!')
       return redirect(url_for('cadastro'))
   novo_jogo = info(nome=nome, categoria=categoria, console=console)
   db.session.add(novo_jogo)
   db.session.commit()

   return redirect(url_for('index'))
@app.route('/tabela')
def tabela():
    return render_template('tabela.html',item=lista)
@app.route('/table', methods = ['POST',])
def table():
    lista = models.info.query.order_by(models.info.cpf)
    return render_template('tabela.html', item=lista)
