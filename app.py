import render
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='Efds11091999.',
        servidor='localhost',
        database='cadastro'
    )

db = SQLAlchemy(app)

class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


@app.route("/")
def login():

    return render_template('/login.html', titulo='login')
@app.route('/cadastro')
def cadastro():
    return render_template('/cadastro.html', titulo="cadastro")
@app.route('/cadastro', methods=['POST,'])
def cadastro():
    nome = request.form['name']
    senha = request.form['password']
    data = request.form['birthday']
    jogos = Jogos.query.filter_by(nome=nome).first()
@app.route('/lista')
def lista_de_produtos():
    if login is True:
        return render_template('/lista.html', titulo='lista')
    else:
        return redirect('/cadastro')
app.run(debug=True)



