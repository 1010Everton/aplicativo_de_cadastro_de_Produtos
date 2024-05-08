import os

from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

from app import app
from views import *
from wtforms import StringField, validators


class formulario_cadastro(FlaskForm):
    nome_do_produto = StringField('nome_do_produto', [validators.DataRequired(), validators.length(min=1, max=50)])
    data_de_validade = StringField('data_de_validade', [validators.DataRequired(), validators.length(min=1, max=50)])
    data_de_fabricacao = StringField('data_de_fabricacao', [validators.DataRequired(), validators.length(min=1, max=50)])
    estoque = StringField('estoque', [validators.DataRequired(), validators.length(min=1, max=50)])
    id = StringField('id', [validators.DataRequired(), validators.length(min=1, max=50)])
    salvar = StringField('Salvar')

class formulario_usuario(FlaskForm):
    name = StringField('Name', [validators.DataRequired(), validators.length(min=1, max=50)])
    email = StringField('email', [validators.DataRequired(), validators.length(min=1, max=50)])
    cpf = StringField('cpf', [validators.DataRequired(), validators.length(min=1, max=50)])
    data_de_nascimento = StringField('data_de_nascimento', [validators.DataRequired(), validators.length(min=1, max=50)])
    password = StringField('password', [validators.DataRequired(), validators.length(min=1, max=50)])
    salvar = StringField('Salvar')
def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo
        return '11503513.jpg'

def delete_imagem(id):
    arquivo = recupera_imagem(id)
    os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))




