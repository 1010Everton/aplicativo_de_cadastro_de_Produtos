from app import db


class dados(db.model):

    cpf =  db.collumn(db.interger, primary_key=True, autoincrement = True )
    nome = db.collumn(db.String(50),nullable =False )
    celular = db.collumn(db.interger,nullable=False)