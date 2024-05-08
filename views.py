import time

from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from sqlalchemy import select
from helper import recupera_imagem, delete_imagem, formulario_usuario, formulario_cadastro
import config
from models import info, produto
from app import app, db

@app.route('/tabela')
def tabela():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('tabela')))

    produtos = produto.query.all()
    return render_template('tabela.html', produtos=produtos)
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

            return redirect(url_for('cadastro_do_produto'))
        else:
            flash("Nome de usuário ou senha inválidos")
            return redirect(url_for('login'))

@app.route('/cadastro')
def cadastro():
    form = formulario_usuario()
    return render_template('cadastro.html' , form=form)
@app.route('/cadastro_do_produto')
def cadastro_do_produto():
    form = formulario_cadastro()
    return render_template('cadastro_de_produto.html', form = form)
@app.route('/cadastro_produto', methods=['POST',])
def cadastro_de_produtos():
    nome_do_produto = request.nome_do_produto.data
    data_de_validade = request.data_de_validade.data
    data_de_fabricacao = request.data_de_fabricacao.data
    estoque = request.estoque.data
    id = request.id.data
    produtos = produto.query.filter_by(id=id).first()
    if produtos:
        flash('produto já existe')
        return redirect(url_for('cadastro_do_produto'))
    insere = produto(nome_do_produto=nome_do_produto,data_de_validade=data_de_validade,data_de_fabricacao=data_de_fabricacao,estoque=estoque,id=id)
    db.session.add(insere)
    db.session.commit()

    arquivo = request.files['arquivo']
    UPLOAD_PATH = app.config['UPLOAD_PATH']
    timestamp = time.time()
    deleta_arquivo = insere.id
    arquivo.save(f'{UPLOAD_PATH}/115035{insere.id}-{timestamp}.jpg')

    return redirect('tabela')
@app.route('/criar', methods=['POST',])
def cadastrar():
    nome = request.name.data
    cpf = request.cpf.data
    email = request.email.data
    senha = request.password.data
    data_de_nascimento = request.data_de_nascimento.data


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
    lista = produto.query.order_by(produto.id)
    return render_template('tabela.html', produto=lista)

@app.route('/atualizar', methods=['POST',])
def atualizar():
    jogo = produto.query.filter_by(id=request.form['id']).first()
    jogo.nome_do_produto = request.form['nome_do_produto']
    jogo.data_de_validade = request.form['data_de_validade']
    jogo.data_de_fabricacao = request.form['data_de_fabricacao']
    jogo.estoque = request.form['estoque']
    jogo.id = request.form['id']

    db.session.add(jogo)
    db.session.commit()

    return redirect(url_for('tabela'))
@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login'))
    produto.query.filter_by(id=id).delete()
    db.session.commit()
    flash('deletado com sucesso')

    return redirect(url_for('tabela'))


@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('tabela')))
    id = produto.query.filter_by(id=id).first()
    capa_produto = recupera_imagem(id)
    return render_template('editar.html', produto=id, cadastro_do_produto=capa_produto, capa_produto=capa_produto)

@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('login'))



