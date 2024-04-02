import render
from flask import Flask, redirect, render_template

app = Flask (__name__)

@app.route("/")
def login ():
    if login is True:
        return redirect('lista.html')
    else:
        print('login invalido')
        return redirect('cadastro.html')
@app.route('/cadastro')
def cadastro():
    return render_template('/cadastro.html', titulo="cadastro")
app.run(debug=True)



