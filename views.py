from flask import render_template, request, redirect, session, flash, url_for
from sqlalchemy import select

from models import info
from app import app, db


@app.route('/')
def login():
    proxima = db.session.query(info.nome).all()
    return render_template('login.html', proxima=proxima)

@app.route('/valida', methods=['POST',])
def validacao():
    usuario = info.query.filter_by(nome=request.form['nome']).first()
    if usuario and request.form['nome'] == usuario.password:
        session['usuario_logado'] = usuario.nome
        flash(usuario.nome + ' logado com sucesso')
        proxima_pagina = request.form['cadastro']
        return redirect(proxima_pagina)
    else:
        flash('Nome de usuário ou senha inválidos')
        return redirect(url_for('login'))

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
@app.route('/criar', methods=['POST',])
def cadastrar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    email = request.form['email']
    data_de_nascimento = request.form['birthday']

    dado = info.query.filter_by(cpf=cpf).first()
    if dado:
        flash('Jogo já existente!')
        return redirect(url_for('cadastro'))

    novo_jogo = info(nome=nome, cpf=cpf, email=email, data_de_nascimento=data_de_nascimento)
    db.session.add(novo_jogo)
    db.session.commit()

    return redirect(url_for('login'))
@app.route('/tabela')
def tabela():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect('/')
    return render_template('tabela.html')
@app.route('/table', methods = ['POST',])
def table():
    lista = info.query.order_by(info.cpf)
    return render_template('tabela.html', item=lista)
