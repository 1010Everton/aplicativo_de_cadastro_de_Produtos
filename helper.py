import os

from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

from app import app
from views import *
from wtforms import StringField, validators


class formulario_usuario(FlaskForm):
    name = StringField('Name', [validators.DataRequired(), validators.length(min=1, max=50)])
    email = StringField('Name', [validators.DataRequired(), validators.length(min=1, max=50)])
    cpf = StringField('Name', [validators.DataRequired(), validators.length(min=1, max=50)])
    data_de_nascimento= StringField('Name', [validators.DataRequired(), validators.length(min=1, max=50)])
    password= StringField('Name', [validators.DataRequired(), validators.length(min=1, max=50)])
    salvar = StringField('Salvar')
def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo
        return '11503513.jpg'

def delete_imagem(id):
    arquivo = recupera_imagem(id)
    os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))




