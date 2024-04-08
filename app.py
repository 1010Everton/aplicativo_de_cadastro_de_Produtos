from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='Efds11091999.',
        servidor='Mysql@localhost:3306',
        database='cadastro'
    )

db = SQLAlchemy(app)
class cadastro(db.Model):
    cpf = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, primary_key=True, nullable=False)
    cpf = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return '<Name %r>' % self.name


@app.route('/')
def inicio():
    return render_template('login.html')
@app.route('/cadastro')
def cadastro():
    return render_template('/cadastro.html')
@app.route('/criar', methods=['POST',])
def criar():
    name = request.form['name']
    password = request.form['password']
    email = request.form['email']
    birthday = request.form['birthday']
    grupo = cadastro.query.filter_by(nome=cadastro).first()
    if grupo:
        print('ja existe esse produto')
    return redirect(url_for('login.html'))
    novo_jogo = cadastro(nome=nome, categoria=categoria, console=console)
    db.session.add(novo_produto)
    db.session.commit()
    return redirect(url_for('login,html'))
@app.route('/lista')
def lista():
   return redirect('/')


app.run(debug=True)



