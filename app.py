from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database_name}'.format(
        username = 'root',
        password = 'Efds11091999.',
        host = 'localhost',
        port = '3306',
        database_name = 'cadastro'
    )

db = SQLAlchemy(app)


@app.route('/')
def login():
    return render_template('login.html')
@app.route('/lista')
def lista():
    return render_template('lista.html')
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
app.route('/cadastrar')
def cadastrar():
    if login ==  :
        return redirect('')

app.run(debug=True)

