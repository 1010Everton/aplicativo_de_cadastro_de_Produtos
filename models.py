

from app import db

class info(db.Model):
        nome = db.Column(db.String(50), nullable=False)
        cpf = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(120), unique=True, nullable=False)
        data_de_nascimento = db.Column(db.Date, unique=True, nullable=False)
def __repr__(self):
    return '<nome %r>' % self.nome
