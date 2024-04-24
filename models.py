

from app import db

class info(db.Model):
        nome = db.Column(db.String(50), nullable=False)
        cpf = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(120), unique=True, nullable=False)
        data_de_nascimento = db.Column(db.Date, unique=True, nullable=False)
        password = db.Column(db.String(120),unique=True, nullable=False )
class produto(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        nome_do_produto = db.Column(db.String(120), unique=True, nullable=False)
        data_de_validade = db.Column(db.Date, nullable=False)
        data_de_fabricacao = db.Column(db.Date, nullable=False)
        estoque = db.Column(db.Integer, nullable=False)


def __repr__(self):
    return '<nome %r>' % self.nome
