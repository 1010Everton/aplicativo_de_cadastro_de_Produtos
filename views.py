from flask import render_template, request, redirect, session, flash, url_for
from sqlalchemy import select

from models import info
from app import app, db

@app.route('/tabela')
def tabela():
    lista = info.query.order_by(info.cpf)
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('tabela')))

    return render_template('tabela.html', registro=lista)
@app.route('/')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/valida', methods=['POST',])
def validacao():
    usuario = info.query.filter_by(nome=request.form['nome']).first()
    if usuario:
        if request.form['password'] == usuario.password:
            session["usuario_logado"] = usuario.nome
            flash(usuario.nome + ' logado com sucesso')

            return redirect (url_for('tabela'))
        else:
            flash("Nome de usuário ou senha inválidos")
            return redirect(url_for('login'))

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
@app.route('/criar', methods=['POST',])
def cadastrar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    email = request.form['email']
    senha = request.form['password']
    data_de_nascimento = request.form['birthday']

    dado = info.query.filter_by(cpf=cpf).first()
    if dado:
        flash('Jogo já existente!')
        return redirect(url_for('cadastro'))

    novo_jogo = info(nome=nome, cpf=cpf, email=email, data_de_nascimento=data_de_nascimento, password=senha)
    db.session.add(novo_jogo)
    db.session.commit()

    return redirect(url_for('login'))

@app.route('/table', methods = ['POST',])
def table():
    lista = info.query.order_by(info.cpf)
    return render_template('tabela.html', item=lista)

@app.route('/atualizar', methods=['POST',])
def atualizar():
    jogo = info.query.filter_by(cpf=request.form['cpf']).first()
    jogo.nome = request.form['nome']
    jogo.cpf = request.form['cpf']
    jogo.birthday = request.form['birthday']
    jogo.email = request.form['email']
    jogo.password = request.form['password']

    db.session.add(jogo)
    db.session.commit()

    return redirect(url_for('tabela'))
@app.route('/deletar/<int:cpf>')
def deletar(cpf):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login'))
    info.query.filter_by(cpf=cpf).delete()
    db.session.commit()
    flash('deletado com sucesso')

    return redirect(url_for('tabela'))


@app.route('/editar/<int:cpf>')
def editar(cpf):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('tabela')))
    ps = info.query.filter_by(cpf=cpf).first()
    return render_template('editar.html', info=ps)
