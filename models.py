

from app import db

class info(db.Model):
        nome = db.Column(db.String(50), nullable=False)
        cpf = db.Column(db.Integer, primary_key=True)
        celular = db.Column(db.String(120), unique=True, nullable=False)
        password = db.Column(db.String(120), unique=True, nullable=False)
def __repr__(self):
    return '<Name %r>' % self.nome